from typing import Any

from llama_index.core.output_parsers.base import StructuredOutput
from llama_index.core.output_parsers.utils import parse_json_markdown
from llama_index.core.types import BaseOutputParser
from llama_index.core.vector_stores.types import VectorStoreQuerySpec


class VectorStoreQueryOutputParser(BaseOutputParser):
    def parse(self, output: str) -> Any:
        json_dict = parse_json_markdown(output)
        query_and_filters = VectorStoreQuerySpec.model_validate(json_dict)

        return StructuredOutput(raw_output=output, parsed_output=query_and_filters)

    def format(self, prompt_template: str) -> str:
        return prompt_template
