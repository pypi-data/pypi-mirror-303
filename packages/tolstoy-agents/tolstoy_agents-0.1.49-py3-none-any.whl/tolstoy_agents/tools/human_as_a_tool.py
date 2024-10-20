from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from typing import List, Optional

class ToolInput(BaseModel):
    question: str = Field(
        ..., description= (
            "Question you ask to human."
            )
    )
    options: List[str] = Field(None, description= (
            "Couple options for a human."
            )
    )


def ask_human(question: str, options: List[str] = None) -> str:
    if options:
        return question + '\n' + 'Options: ' + '\n'.join(options)
    return question


def human_tool_factory() -> StructuredTool:
    return StructuredTool.from_function(
        func=ask_human,
        name="ask_human",
        description= (
            "You can ask a human support when you cant fulfill the task. " 
            "Identify what missed or not clarified items you need "
            "to clarify and ask one at a time. Don't assume human response. "
            "When asking, propose 2 possible reply options that user may want to choose."
        ),
        args_schema=ToolInput,
        return_direct=False
    )
