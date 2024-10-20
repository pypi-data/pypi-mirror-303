import json

from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from tolstoy_agents.linear import query_issue

class ToolInput(BaseModel):
    issue_id: str = Field(
        description="id of the linear issue."
    )


def query_linear_issue(issue_id: str) -> str:
    print(f"Querying linear issue with id: {issue_id}")
    res = query_issue(issue_id)
    
    print(type(res), res)
    if isinstance(res, dict):
        return json.dumps(res)
    return str(res)


def query_linear_issue_factory() -> StructuredTool:
    return StructuredTool.from_function(
        query_linear_issue,
        name="query_linear_issue",
        description= (
            "Use this tool to get information of specific linear issue." 
        ),
        args_schema=ToolInput,
        return_direct=False
    )
