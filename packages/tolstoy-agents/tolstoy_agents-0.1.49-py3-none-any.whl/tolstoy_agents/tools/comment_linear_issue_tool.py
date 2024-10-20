import json

from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from tolstoy_agents.linear import create_comment


class ToolInput(BaseModel):
    issue_id: str = Field(
        description="id of the linear issue."
    )
    comment_text: str = Field(
        description="text to add as a comment to issue."
    )


def comment_issue(issue_id: str, comment_text:str) -> str:
    print(f"Atempting to comment on linear issue with id: {issue_id}")
    res = create_comment(issue_id, comment_text)
    return str(res)


def comment_issue_factory() -> StructuredTool:
    return StructuredTool.from_function(
        comment_issue,
        name="comment_issue",
        description= (
            "Use this tool to add comment to the issue in Linear." 
        ),
        args_schema=ToolInput,
        return_direct=False
    )
