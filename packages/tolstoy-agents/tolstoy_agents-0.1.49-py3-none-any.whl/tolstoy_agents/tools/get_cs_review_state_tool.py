import os
import json
import functools
from pydantic import BaseModel, Field
import boto3

from langchain.tools import StructuredTool

from tolstoy_agents.utils import (
    handle_exceptions
    )

lambda_client = boto3.client('lambda')

class ToolInput(BaseModel):
    tolstoy_user_email: str = Field(description="Email of Tolstoy's customer")

@handle_exceptions
def get_cs_review_state(tolstoy_user_email: str) -> str:
    
    function_name = f"tolstoy-customer-transcripts-{os.environ['env']}-getCsmReviewState"
    payload = json.dumps({"body": json.dumps({"customer": {"email": tolstoy_user_email}})})
    
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=payload
    )
    
    if response.get('StatusCode') == 200:
        response_payload = json.loads(response['Payload'].read())
        return json.dumps(response_payload)
    else:
        return ""


def get_cs_review_state_factory() -> StructuredTool:
    return StructuredTool.from_function(
        func=get_cs_review_state,
        name="get_cs_review_state",
        description= (
            "Use this tool to get a comprehensive view of the customer's status and potential issues. "
            "Sometimes a customer may not have a CS review state, and in such cases, this tool will return an empty string, which is acceptable."
        ),
        args_schema=ToolInput,
        return_direct=False
    )
