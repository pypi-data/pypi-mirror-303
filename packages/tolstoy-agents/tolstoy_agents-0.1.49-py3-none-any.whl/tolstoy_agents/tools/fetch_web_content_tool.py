import os
import json
import functools
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool

from tolstoy_agents.utils import (
    handle_exceptions
    )

from tolstoy_agents.tools.web_base_loader import WebBaseLoaderScraper


class ToolInput(BaseModel):
    url: str = Field(description="url of the web page")


@handle_exceptions
def fetch_web_content(url: str,
                ) -> str:
    loader = WebBaseLoaderScraper()
    content = loader.scrape(url)

    return content


def fetch_web_content_factory() -> StructuredTool:
    return StructuredTool.from_function(
        func=fetch_web_content,
        name="fetch_web_content",
        description= (
            "Use this tool to get content from web url."
        ),
        args_schema=ToolInput,
        return_direct=False
    )
