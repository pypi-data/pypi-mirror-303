import os
import json
import re
import boto3
import functools
import logging
from pydantic import BaseModel, Field
from enum import Enum
from typing import (
    Annotated,
    Sequence,
    TypedDict,
    List,
    Union,
    Optional,
    Callable,
    Any,
    Dict,
    Type
    )

from langchain.schema import AIMessage
from langchain_core.tools import BaseTool
from langchain.schema import Document
from langsmith.utils import LangSmithNotFoundError

from tolstoy_agents.google_spreadsheet import search_and_get_adjacent_value

ssm_client = boto3.client("ssm", region_name='us-east-1')

class Environment(str, Enum):
    dev = "dev"
    eval = "eval"
    prod = "prod"

logger = logging.getLogger()
if logger.hasHandlers():
    logger.setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)


def message_to_sns(payload_to_sns: dict,
                   topic_arn=None,
                   session_id=None,
                   task_id=None,
                   user_id=None)->str:
    if not payload_to_sns.get('message'):
        return f"Empty message to sns"
    
    if not topic_arn:
        topic_arn = os.environ.get('AGENTS_ROUTER_TOPIC_ARN')
    if not topic_arn:
        return 'No AGENTS_ROUTER_TOPIC_ARN set'
    
    if session_id:
        payload_to_sns['session_id'] = session_id
    if task_id:
        payload_to_sns['task_id'] = task_id
    if user_id:
        payload_to_sns['user_id'] = user_id

    print(f"Sending message to sns: {payload_to_sns}")
    
    keys = list(payload_to_sns.keys())
    for key in keys:
        if not payload_to_sns[key]:
            del payload_to_sns[key]

    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(payload_to_sns)
    )

    if response['ResponseMetadata']['HTTPStatusCode']!=200:
        return f"Failed to send msg to SNS: {response}"

    return payload_to_sns['message']


def get_ssm_param(param_name: str, env: Environment) -> str:
    param_name = f"{env.value}_{param_name}"
    
    try:
        res = ssm_client.get_parameter(Name=param_name, WithDecryption=True)["Parameter"][
            "Value"
        ]
    except Exception as exception:
        raise Exception(f"Failed to retrieve the SSM parameter: {param_name}") from exception
    
    return res


def log(message):
    logger.info(message)


def log_lumigo_error(message, type):
    lumigo_error = {"message": message, "type": type}

    logger.info(f"[LUMIGO_LOG] {json.dumps(lumigo_error)}")


def log_lumigo_exception(exception, type):
    return log_lumigo_error(str(exception) or "Exception was thrown", type)


class MessageReasoningResponse(BaseModel):
    reasoning: str = Field(
        description="Reasoning of your answer"
    )
    destination: str = Field(
        description="Destination of the message: User or <tool_name>"
    )
    message: Union[str, Dict] = Field(
        description="Message to User or dict with args to invoke a tool"
    )


def scratchpad_to_msgs(
        intermediate_steps, name
    ):
    msgs = []
    for action, observation in intermediate_steps:
        msgs.append(AIMessage(content=action.log, name=name))
        msgs.append(AIMessage(content=observation, name='Tool'))
    return msgs


def get_langsmith_url(cb):
    from langsmith import Client

    run_id = cb.traced_runs[0].id if cb.traced_runs else None

    langsmith_url = ""
    if run_id:
        try:
            client = Client()
            run = client.read_run(run_id)
            langsmith_url = run.url
            # Remove the start_time parameter from the URL
            langsmith_url = re.sub(r'&start_time=[^&]+', '', langsmith_url)
        except LangSmithNotFoundError:
            print(f"Run with ID {run_id} not found in LangSmith")
            langsmith_url = f"Run not found: {run_id}"
    
    return langsmith_url


def custom_render_tools(tools):
    formatted_tools = []
    for index, tool in enumerate(tools, start=1):
        tool_string = f"{index}. {tool.name}:\n"
        tool_string += f"Description:\n   {tool.description}\n\n"
        
        if hasattr(tool, 'args_schema'):
            args = tool.args_schema.schema()['properties']
            tool_string += "Arguments:\n"
            for arg_name, arg_info in args.items():
                tool_string += f"       - {arg_name}: {arg_info.get('type', 'any')}\n"
        
        formatted_tools.append(tool_string)
    
    return "\n".join(formatted_tools).strip()


def docs_to_text(relevant_docs: List[Document]):
    res = []
    for doc in relevant_docs:
        res.append(f"filepath: {doc.metadata['filepath']}\n\n{doc.page_content}")

    res = '\n\n'.join(res)

    return res


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper


def custom_render_text_description_and_args(tools: List[BaseTool], short = False, index = True) -> str:
    """Render the tool name, description, and args in plain text.

    Output will be in the format of:

    .. code-block:: markdown

        search: This tool is used for search, args: {"query": {"type": "string"}}
        calculator: This tool is used for math, \
    args: {"expression": {"type": "string"}}
    """
    tool_strings = []
    for ix, tool in enumerate(tools):
        args_schema = tool.args
        try:
            if '->' in tool.description:
                description = tool.description.split('->', maxsplit=1)[1].split('-', maxsplit=1)[1].strip()
            else:
                description = tool.description.split('-', maxsplit=1)[1].strip()
        except Exception:
            description = tool.description

        if short:
            if index:
                line = f"{ix+1}. {tool.name}: {description}"
            else:
                line = f"{tool.name}: {description}"
            tool_strings.append(line)
        else:
            tool_strings.append(f"{ix+1}. {tool.name}: {description},\nargs: ")
            for key, value in args_schema.items():
                if 'anyOf' in value:
                    value_type = ' | '.join([option['type'] for option in value['anyOf']])
                else:
                    value_type = value['type']
                tool_string = f"    {key}: {value_type}"
                if 'items' in value:
                    if 'type' in value['items']:
                        tool_string += f"[{value['items']['type']}]"
                tool_string += f" # {value['description']}"
                tool_strings.append(tool_string)
        #tool_strings.append(f"{tool.name}: {args_schema}")
    return "\n".join(tool_strings) + "\n"

def dynamic_tools_name(tools):
    for tool in tools:
        tool.description = search_and_get_adjacent_value(AGENT_TOOLS_SPREADSHEET_ID, TASKS_AGENT_SHEET, tool.name)
    return tools