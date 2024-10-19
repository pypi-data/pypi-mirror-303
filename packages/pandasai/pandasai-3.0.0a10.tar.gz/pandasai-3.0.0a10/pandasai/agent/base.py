import os
import re
import uuid
from typing import List, Optional, Union

import pandasai.pandas as pd
from pandasai.agent.base_security import BaseSecurity
from pandasai.llm.bamboo_llm import BambooLLM
from pandasai.pipelines.chat.chat_pipeline_input import ChatPipelineInput
from pandasai.pipelines.chat.code_execution_pipeline_input import (
    CodeExecutionPipelineInput,
)
from pandasai.vectorstores.vectorstore import VectorStore

from ..config import load_config_from_json
from ..connectors import BaseConnector, PandasConnector
from ..constants import DEFAULT_CACHE_DIRECTORY, DEFAULT_CHART_DIRECTORY
from ..exceptions import (
    InvalidLLMOutputType,
    MaliciousQueryError,
    MissingVectorStoreError,
)
from ..helpers.df_info import df_type
from ..helpers.folder import Folder
from ..helpers.logger import Logger
from ..helpers.memory import Memory
from ..llm.base import LLM
from importlib.util import find_spec
from ..pipelines.pipeline_context import PipelineContext
from ..prompts.base import BasePrompt
from ..schemas.df_config import Config
from .callbacks import Callbacks


class BaseAgent:
    """
    Base Agent class to improve the conversational experience in PandasAI
    """

    def __init__(
        self,
        dfs: Union[
            pd.DataFrame, BaseConnector, List[Union[pd.DataFrame, BaseConnector]]
        ],
        config: Optional[Union[Config, dict]] = None,
        memory_size: Optional[int] = 10,
        vectorstore: Optional[VectorStore] = None,
        description: str = None,
        security: BaseSecurity = None,
    ):
        """
        Args:
            df (Union[pd.DataFrame, List[pd.DataFrame]]): Pandas or Modin dataframe or Database connectors
            memory_size (int, optional): Conversation history to use during chat.
            Defaults to 1.
        """
        self.last_prompt = None
        self.last_prompt_id = None
        self.last_result = None
        self.last_code_generated = None
        self.last_code_executed = None
        self.agent_info = description

        self.conversation_id = uuid.uuid4()

        self.dfs = self.get_dfs(dfs)

        # Instantiate the context
        self.config = self.get_config(config)
        self.context = PipelineContext(
            dfs=self.dfs,
            config=self.config,
            memory=Memory(memory_size, agent_info=description),
            vectorstore=vectorstore,
        )

        # Instantiate the logger
        self.logger = Logger(
            save_logs=self.config.save_logs, verbose=self.config.verbose
        )

        # Instantiate the vectorstore
        self._vectorstore = vectorstore

        if self._vectorstore is None and os.environ.get("PANDASAI_API_KEY"):
            try:
                from pandasai.vectorstores.bamboo_vectorstore import BambooVectorStore
            except ImportError as e:
                raise ImportError(
                    "Could not import BambooVectorStore. Please install the required dependencies."
                ) from e

            self._vectorstore = BambooVectorStore(logger=self.logger)
            self.context.vectorstore = self._vectorstore

        self._callbacks = Callbacks(self)

        self.configure()

        self.pipeline = None
        self.security = security

    def configure(self):
        # Add project root path if save_charts_path is default
        if (
            self.config.save_charts
            and self.config.save_charts_path == DEFAULT_CHART_DIRECTORY
        ):
            Folder.create(self.config.save_charts_path)

        # Add project root path if cache_path is default
        if self.config.enable_cache:
            Folder.create(DEFAULT_CACHE_DIRECTORY)

    def get_config(self, config: Union[Config, dict]):
        """
        Load a config to be used to run the queries.

        Args:
            config (Union[Config, dict]): Config to be used
        """

        config = load_config_from_json(config)

        if isinstance(config, dict) and config.get("llm") is not None:
            config["llm"] = self.get_llm(config["llm"])

        config = Config(**config)

        if config.llm is None:
            config.llm = BambooLLM()

        return config

    def get_llm(self, llm: LLM) -> LLM:
        """
        Load a LLM to be used to run the queries.
        Check if it is a PandasAI LLM or a Langchain LLM.
        If it is a Langchain LLM, wrap it in a PandasAI LLM.

        Args:
            llm (object): LLMs option to be used for API access

        Raises:
            BadImportError: If the LLM is a Langchain LLM but the langchain package
            is not installed
        """
        # Check if pandasai_langchain is installed
        if find_spec("pandasai_langchain") is not None:
            from pandasai_langchain.langchain import LangchainLLM, is_langchain_llm

            if is_langchain_llm(llm):
                llm = LangchainLLM(llm)

        return llm

    def get_dfs(
        self,
        dfs: Union[
            pd.DataFrame, BaseConnector, List[Union[pd.DataFrame, BaseConnector]]
        ],
    ):
        """
        Load all the dataframes to be used in the agent.

        Args:
            dfs (List[Union[pd.DataFrame, Any]]): Pandas dataframe
        """
        # Inline import to avoid circular import
        from pandasai.smart_dataframe import SmartDataframe

        # If only one dataframe is passed, convert it to a list
        if not isinstance(dfs, list):
            dfs = [dfs]

        connectors = []
        for df in dfs:
            if isinstance(df, BaseConnector):
                connectors.append(df)
            elif isinstance(df, (pd.DataFrame, pd.Series, list, dict, str)):
                connectors.append(PandasConnector({"original_df": df}))
            elif df_type(df) == "modin":
                connectors.append(PandasConnector({"original_df": df}))
            elif isinstance(df, SmartDataframe) and isinstance(
                df.dataframe, BaseConnector
            ):
                connectors.append(df.dataframe)
            else:
                raise ValueError(
                    "Invalid input data. We cannot convert it to a dataframe."
                )
        return connectors

    def call_llm_with_prompt(self, prompt: BasePrompt):
        """
        Call LLM with prompt using error handling to retry based on config
        Args:
            prompt (BasePrompt): BasePrompt to pass to LLM's
        """
        retry_count = 0
        while retry_count < self.context.config.max_retries:
            try:
                result: str = self.context.config.llm.call(prompt)
                if prompt.validate(result):
                    return result
                else:
                    raise InvalidLLMOutputType("Response validation failed!")
            except Exception:
                if (
                    not self.context.config.use_error_correction_framework
                    or retry_count >= self.context.config.max_retries - 1
                ):
                    raise
                retry_count += 1

    def check_malicious_keywords_in_query(self, query):
        dangerous_pattern = re.compile(
            r"\b(os|io|chr|b64decode)\b|"
            r"(\.os|\.io|'os'|'io'|\"os\"|\"io\"|chr\(|chr\)|chr |\(chr)"
        )
        return bool(dangerous_pattern.search(query))

    def chat(self, query: str, output_type: Optional[str] = None):
        """
        Start a new chat interaction with the assistant on Dataframe.
        """
        self.start_new_conversation()
        return self._process_query(query, output_type)

    def follow_up(self, query: str, output_type: Optional[str] = None):
        """
        Continue the existing chat interaction with the assistant on Dataframe.
        """
        return self._process_query(query, output_type)

    def _process_query(self, query: str, output_type: Optional[str] = None):
        """
        Process a query and return the result.
        """
        if not self.pipeline:
            return (
                "Unfortunately, I was not able to get your answers, "
                "because of the following error: No pipeline exists"
            )

        try:
            self.logger.log(f"Question: {query}")
            self.logger.log(
                f"Running PandasAI with {self.context.config.llm.type} LLM..."
            )

            self.assign_prompt_id()

            if self.check_malicious_keywords_in_query(query):
                raise MaliciousQueryError(
                    "The query contains references to io or os modules or b64decode method which can be used to execute or access system resources in unsafe ways."
                )

            if self.security and self.security.evaluate(query):
                raise MaliciousQueryError("Query can result in a malicious code")

            pipeline_input = ChatPipelineInput(
                query, output_type, self.conversation_id, self.last_prompt_id
            )

            return self.pipeline.run(pipeline_input)

        except Exception as exception:
            return (
                "Unfortunately, I was not able to get your answers, "
                "because of the following error:\n"
                f"\n{exception}\n"
            )

    def generate_code(self, query: str, output_type: Optional[str] = None):
        """
        Simulate code generation with the assistant on Dataframe.
        """
        if not self.pipeline:
            return (
                "Unfortunately, I was not able to get your answers, "
                "because of the following error: No pipeline exists"
            )
        try:
            self.logger.log(f"Question: {query}")
            self.logger.log(
                f"Running PandasAI with {self.context.config.llm.type} LLM..."
            )

            self.assign_prompt_id()

            pipeline_input = ChatPipelineInput(
                query, output_type, self.conversation_id, self.last_prompt_id
            )

            return self.pipeline.run_generate_code(pipeline_input)
        except Exception as exception:
            return (
                "Unfortunately, I was not able to get your answers, "
                "because of the following error:\n"
                f"\n{exception}\n"
            )

    def execute_code(
        self, code: Optional[str] = None, output_type: Optional[str] = None
    ):
        """
        Execute code Generated with the assistant on Dataframe.
        """
        if not self.pipeline:
            return (
                "Unfortunately, I was not able to get your answers, "
                "because of the following error: No pipeline exists to execute try Agent class"
            )
        try:
            if code is None:
                code = self.last_code_generated
            self.logger.log(f"Code: {code}")
            self.logger.log(
                f"Running PandasAI with {self.context.config.llm.type} LLM..."
            )

            self.assign_prompt_id()

            pipeline_input = CodeExecutionPipelineInput(
                code, output_type, self.conversation_id, self.last_prompt_id
            )

            return self.pipeline.run_execute_code(pipeline_input)
        except Exception as exception:
            return (
                "Unfortunately, I was not able to get your answers, "
                "because of the following error:\n"
                f"\n{exception}\n"
            )

    def train(
        self,
        queries: Optional[List[str]] = None,
        codes: Optional[List[str]] = None,
        docs: Optional[List[str]] = None,
    ) -> None:
        """
        Trains the context to be passed to model
        Args:
            queries (Optional[str], optional): user user
            codes (Optional[str], optional): generated code
            docs (Optional[List[str]], optional): additional docs
        Raises:
            ImportError: if default vector db lib is not installed it raises an error
        """
        if self._vectorstore is None:
            raise MissingVectorStoreError(
                "No vector store provided. Please provide a vector store to train the agent."
            )

        if (queries and not codes) or (not queries and codes):
            raise ValueError(
                "If either queries or codes are provided, both must be provided."
            )

        if docs is not None:
            self._vectorstore.add_docs(docs)

        if queries and codes:
            self._vectorstore.add_question_answer(queries, codes)

        self.logger.log("Agent successfully trained on the data")

    def clear_memory(self):
        """
        Clears the memory
        """
        self.context.memory.clear()
        self.conversation_id = uuid.uuid4()

    def add_message(self, message, is_user=False):
        """
        Add message to the memory. This is useful when you want to add a message
        to the memory without calling the chat function (for example, when you
        need to add a message from the agent).
        """
        self.context.memory.add(message, is_user=is_user)

    def assign_prompt_id(self):
        """Assign a prompt ID"""

        self.last_prompt_id = uuid.uuid4()

        if self.logger:
            self.logger.log(f"Prompt ID: {self.last_prompt_id}")

    def start_new_conversation(self):
        """
        Clears the previous conversation
        """
        self.clear_memory()

    @property
    def logs(self):
        return self.logger.logs

    @property
    def last_error(self):
        raise NotImplementedError

    @property
    def last_query_log_id(self):
        raise NotImplementedError
