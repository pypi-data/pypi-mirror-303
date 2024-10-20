from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from typing import List, Optional

class SupportToolInput(BaseModel):
    internal_question: str = Field(
        ..., description="Question to ask the internal support team. This will be sent to our internal slack channel that these two members <@U048F72HN6B> and <@U048SQJB8TF> manage. Always start your message with these two EXACT tags <@U048F72HN6B><@U048SQJB8TF> to mention both of these internal team members, It should always be both of member ID. THIS IS MANDATORY"
    )
    user_message: str = Field(
        ..., description="Message to display to the user while waiting for internal support. This will be sent to the user as a reply to their message. Don't reveal you're consulting others, just say you're looking into it or checking internally."
    )

def ask_support(internal_question: str, user_message: str) -> str:
    return f"INTERNAL: {internal_question}\nUSER: {user_message}"

def support_human_tool_factory() -> StructuredTool:
    return StructuredTool.from_function(
        func=ask_support,
        name="ask_internal_support",
        description=(
            "Use this tool when you need to check something internally or require "
            "assistance from the internal team. Provide both the internal question that contains the EXACT tags <@U048F72HN6B><@U048SQJB8TF> to mention both of these internal team members"
            "and a message for the user that doesn't reveal you're consulting others."
            "You can use this tool to ask the internal team to answer a question that you don't know because the context you have is not enough, or to do something that you don't have ability, tell internal team about the user's request."
        ),
        args_schema=SupportToolInput,
        return_direct=False
    )
