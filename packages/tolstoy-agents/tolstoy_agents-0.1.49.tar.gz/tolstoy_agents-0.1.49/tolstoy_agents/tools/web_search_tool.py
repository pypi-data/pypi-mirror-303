import functools
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from tolstoy_agents.utils import handle_exceptions
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search.tool import TavilySearchResults

tavily_tool = TavilySearchResults(api_wrapper= TavilySearchAPIWrapper(), max_results=3)

class ToolInput(BaseModel):
    query: str = Field(..., description=(
        "query to search in web."
        )
    )


@handle_exceptions
def web_search_tool(query: str) -> str:
    res = tavily_tool.invoke({"query": query})

    res = [f"{r['url']}\n-----------\n{r['content']}\n\n" for r in res]

    return "\n".join(res)


def web_search_tool_factory() -> StructuredTool:
    return StructuredTool.from_function(
        func=web_search_tool,
        name="web_search_tool",
        description= (
            "Use this tool to search answers in internet."
        ),
        args_schema=ToolInput,
        return_direct=False
    )
