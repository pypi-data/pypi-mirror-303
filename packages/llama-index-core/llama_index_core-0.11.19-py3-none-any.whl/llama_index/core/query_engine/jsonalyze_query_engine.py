import asyncio
import json
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple

from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.core.base.response.schema import Response
from llama_index.core.indices.struct_store.sql_retriever import (
    BaseSQLParser,
    DefaultSQLParser,
)
from llama_index.core.llms.llm import LLM
from llama_index.core.prompts import BasePromptTemplate, PromptTemplate
from llama_index.core.prompts.default_prompts import DEFAULT_JSONALYZE_PROMPT
from llama_index.core.prompts.mixin import PromptDictType, PromptMixinType
from llama_index.core.prompts.prompt_type import PromptType
from llama_index.core.schema import QueryBundle
from llama_index.core.settings import Settings
from llama_index.core.utils import print_text

logger = logging.getLogger(__name__)

DEFAULT_RESPONSE_SYNTHESIS_PROMPT_TMPL = (
    "Given a query, synthesize a response based on SQL query results"
    " to satisfy the query. Only include details that are relevant to"
    " the query. If you don't know the answer, then say that.\n"
    "SQL Query: {sql_query}\n"
    "Table Schema: {table_schema}\n"
    "SQL Response: {sql_response}\n"
    "Query: {query_str}\n"
    "Response: "
)

DEFAULT_RESPONSE_SYNTHESIS_PROMPT = PromptTemplate(
    DEFAULT_RESPONSE_SYNTHESIS_PROMPT_TMPL,
    prompt_type=PromptType.SQL_RESPONSE_SYNTHESIS,
)

DEFAULT_TABLE_NAME = "items"


def default_jsonalyzer(
    list_of_dict: List[Dict[str, Any]],
    query_bundle: QueryBundle,
    llm: LLM,
    table_name: str = DEFAULT_TABLE_NAME,
    prompt: BasePromptTemplate = DEFAULT_JSONALYZE_PROMPT,
    sql_parser: BaseSQLParser = DefaultSQLParser(),
) -> Tuple[str, Dict[str, Any], List[Dict[str, Any]]]:
    """Default JSONalyzer that executes a query on a list of dictionaries.

    Args:
        list_of_dict (List[Dict[str, Any]]): List of dictionaries to query.
        query_bundle (QueryBundle): The query bundle.
        llm (LLM): The llm to use.
        table_name (str): The table name to use, defaults to DEFAULT_TABLE_NAME.
        prompt (BasePromptTemplate): The prompt to use.
        sql_parser (BaseSQLParser): The SQL parser to use.

    Returns:
        Tuple[str, Dict[str, Any], List[Dict[str, Any]]]: The SQL Query,
            the Schema, and the Result.
    """
    try:
        import sqlite_utils  # pants: no-infer-dep
    except ImportError as exc:
        IMPORT_ERROR_MSG = (
            "sqlite-utils is needed to use this Query Engine:\n"
            "pip install sqlite-utils"
        )

        raise ImportError(IMPORT_ERROR_MSG) from exc
    # Instantiate in-memory SQLite database
    db = sqlite_utils.Database(memory=True)
    try:
        # Load list of dictionaries into SQLite database
        db[table_name].insert_all(list_of_dict)  # type: ignore
    except sqlite_utils.utils.sqlite3.IntegrityError as exc:
        print_text(f"Error inserting into table {table_name}, expected format:")
        print_text("[{col1: val1, col2: val2, ...}, ...]")
        raise ValueError("Invalid list_of_dict") from exc

    # Get the table schema
    table_schema = db[table_name].columns_dict

    query = query_bundle.query_str
    prompt = prompt or DEFAULT_JSONALYZE_PROMPT
    # Get the SQL query with text-to-SQL prompt
    response_str = llm.predict(
        prompt=prompt,
        table_name=table_name,
        table_schema=table_schema,
        question=query,
    )

    sql_parser = sql_parser or DefaultSQLParser()

    sql_query = sql_parser.parse_response_to_sql(response_str, query_bundle)

    try:
        # Execute the SQL query
        results = list(db.query(sql_query))
    except sqlite_utils.utils.sqlite3.OperationalError as exc:
        print_text(f"Error executing query: {sql_query}")
        raise ValueError("Invalid query") from exc

    return sql_query, table_schema, results


async def async_default_jsonalyzer(
    list_of_dict: List[Dict[str, Any]],
    query_bundle: QueryBundle,
    llm: LLM,
    prompt: Optional[BasePromptTemplate] = None,
    sql_parser: Optional[BaseSQLParser] = None,
    table_name: str = DEFAULT_TABLE_NAME,
) -> Tuple[str, Dict[str, Any], List[Dict[str, Any]]]:
    """Default JSONalyzer.

    Args:
        list_of_dict (List[Dict[str, Any]]): List of dictionaries to query.
        query_bundle (QueryBundle): The query bundle.
        llm (LLM): The llm to use.
        prompt (BasePromptTemplate, optional): The prompt to use.
        sql_parser (BaseSQLParser, optional): The SQL parser to use.
        table_name (str, optional): The table name to use, defaults to DEFAULT_TABLE_NAME.

    Returns:
        Tuple[str, Dict[str, Any], List[Dict[str, Any]]]: The SQL Query,
            the Schema, and the Result.
    """
    try:
        import sqlite_utils  # pants: no-infer-dep
    except ImportError as exc:
        IMPORT_ERROR_MSG = (
            "sqlite-utils is needed to use this Query Engine:\n"
            "pip install sqlite-utils"
        )

        raise ImportError(IMPORT_ERROR_MSG) from exc
    # Instantiate in-memory SQLite database
    db = sqlite_utils.Database(memory=True)
    try:
        # Load list of dictionaries into SQLite database
        db[table_name].insert_all(list_of_dict)  # type: ignore
    except sqlite_utils.utils.sqlite3.IntegrityError as exc:
        print_text(f"Error inserting into table {table_name}, expected format:")
        print_text("[{col1: val1, col2: val2, ...}, ...]")
        raise ValueError("Invalid list_of_dict") from exc

    # Get the table schema
    table_schema = db[table_name].columns_dict

    query = query_bundle.query_str
    prompt = prompt or DEFAULT_JSONALYZE_PROMPT
    # Get the SQL query with text-to-SQL prompt
    response_str = await llm.apredict(
        prompt=prompt,
        table_name=table_name,
        table_schema=table_schema,
        question=query,
    )

    sql_parser = sql_parser or DefaultSQLParser()

    sql_query = sql_parser.parse_response_to_sql(response_str, query_bundle)

    try:
        # Execute the SQL query
        results = list(db.query(sql_query))
    except sqlite_utils.utils.sqlite3.OperationalError as exc:
        print_text(f"Error executing query: {sql_query}")
        raise ValueError("Invalid query") from exc

    return sql_query, table_schema, results


def load_jsonalyzer(
    use_async: bool = False,
    custom_jsonalyzer: Optional[Callable] = None,
) -> Callable:
    """Load the JSONalyzer.

    Args:
        use_async (bool): Whether to use async.
        custom_jsonalyzer (Callable): A custom JSONalyzer to use.

    Returns:
        Callable: The JSONalyzer.
    """
    if custom_jsonalyzer:
        assert not use_async or asyncio.iscoroutinefunction(
            custom_jsonalyzer
        ), "custom_jsonalyzer function must be async when use_async is True"
        return custom_jsonalyzer
    else:
        # make mypy happy to indent this
        if use_async:
            return async_default_jsonalyzer
        else:
            return default_jsonalyzer


class JSONalyzeQueryEngine(BaseQueryEngine):
    """JSON List Shape Data Analysis Query Engine.

    Converts natural language statasical queries to SQL within in-mem SQLite queries.

    list_of_dict(List[Dict[str, Any]]): List of dictionaries to query.
    jsonalyze_prompt (BasePromptTemplate): The JSONalyze prompt to use.
    use_async (bool): Whether to use async.
    analyzer (Callable): The analyzer that executes the query.
    sql_parser (BaseSQLParser): The SQL parser that ensures valid SQL being parsed
        from llm output.
    synthesize_response (bool): Whether to synthesize a response.
    response_synthesis_prompt (BasePromptTemplate): The response synthesis prompt
        to use.
    table_name (str): The table name to use.
    verbose (bool): Whether to print verbose output.
    """

    def __init__(
        self,
        list_of_dict: List[Dict[str, Any]],
        llm: Optional[LLM] = None,
        jsonalyze_prompt: Optional[BasePromptTemplate] = None,
        use_async: bool = False,
        analyzer: Optional[Callable] = None,
        sql_parser: Optional[BaseSQLParser] = None,
        synthesize_response: bool = True,
        response_synthesis_prompt: Optional[BasePromptTemplate] = None,
        table_name: str = DEFAULT_TABLE_NAME,
        verbose: bool = False,
        **kwargs: Any,
    ) -> None:
        """Initialize params."""
        self._list_of_dict = list_of_dict
        self._llm = llm or Settings.llm
        self._jsonalyze_prompt = jsonalyze_prompt or DEFAULT_JSONALYZE_PROMPT
        self._use_async = use_async
        self._analyzer = load_jsonalyzer(use_async, analyzer)
        self._sql_parser = sql_parser or DefaultSQLParser()
        self._synthesize_response = synthesize_response
        self._response_synthesis_prompt = (
            response_synthesis_prompt or DEFAULT_RESPONSE_SYNTHESIS_PROMPT
        )
        self._table_name = table_name
        self._verbose = verbose

        super().__init__(callback_manager=Settings.callback_manager)

    def _get_prompts(self) -> Dict[str, Any]:
        """Get prompts."""
        return {
            "jsonalyze_prompt": self._jsonalyze_prompt,
            "response_synthesis_prompt": self._response_synthesis_prompt,
        }

    def _update_prompts(self, prompts: PromptDictType) -> None:
        """Update prompts."""
        if "jsonalyze_prompt" in prompts:
            self._jsonalyze_prompt = prompts["jsonalyze_prompt"]
        if "response_synthesis_prompt" in prompts:
            self._response_synthesis_prompt = prompts["response_synthesis_prompt"]

    def _get_prompt_modules(self) -> PromptMixinType:
        """Get prompt sub-modules."""
        return {}

    def _query(self, query_bundle: QueryBundle) -> Response:
        """Answer an analytical query on the JSON List."""
        query = query_bundle.query_str
        if self._verbose:
            print_text(f"Query: {query}\n", color="green")

        # Perform the analysis
        sql_query, table_schema, results = self._analyzer(
            self._list_of_dict,
            query_bundle,
            self._llm,
            table_name=self._table_name,
            prompt=self._jsonalyze_prompt,
            sql_parser=self._sql_parser,
        )
        if self._verbose:
            print_text(f"SQL Query: {sql_query}\n", color="blue")
            print_text(f"Table Schema: {table_schema}\n", color="cyan")
            print_text(f"SQL Response: {results}\n", color="yellow")

        if self._synthesize_response:
            response_str = self._llm.predict(
                self._response_synthesis_prompt,
                sql_query=sql_query,
                table_schema=table_schema,
                sql_response=results,
                query_str=query_bundle.query_str,
            )
            if self._verbose:
                print_text(f"Response: {response_str}", color="magenta")
        else:
            response_str = str(results)
        response_metadata = {"sql_query": sql_query, "table_schema": str(table_schema)}

        return Response(response=response_str, metadata=response_metadata)

    async def _aquery(self, query_bundle: QueryBundle) -> Response:
        """Answer an analytical query on the JSON List."""
        query = query_bundle.query_str
        if self._verbose:
            print_text(f"Query: {query}", color="green")

        # Perform the analysis
        sql_query, table_schema, results = self._analyzer(
            self._list_of_dict,
            query,
            self._llm,
            table_name=self._table_name,
            prompt=self._jsonalyze_prompt,
        )
        if self._verbose:
            print_text(f"SQL Query: {sql_query}\n", color="blue")
            print_text(f"Table Schema: {table_schema}\n", color="cyan")
            print_text(f"SQL Response: {results}\n", color="yellow")

        if self._synthesize_response:
            response_str = await self._llm.apredict(
                self._response_synthesis_prompt,
                sql_query=sql_query,
                table_schema=table_schema,
                sql_response=results,
                query_str=query_bundle.query_str,
            )
            if self._verbose:
                print_text(f"Response: {response_str}", color="magenta")
        else:
            response_str = json.dumps(
                {
                    "sql_query": sql_query,
                    "table_schema": table_schema,
                    "sql_response": results,
                }
            )
        response_metadata = {"sql_query": sql_query, "table_schema": str(table_schema)}

        return Response(response=response_str, metadata=response_metadata)
