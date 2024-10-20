from typing import (
    List,
    Callable
    )
from pydantic import BaseModel, Field
from langchain.schema import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models import BaseLanguageModel
from langchain.tools import StructuredTool
from langchain_core.runnables import Runnable

from tolstoy_agents.utils import custom_render_text_description_and_args, custom_render_tools


class ToolMessage(BaseModel):
    tool_name: str = Field(description="The name of the Tool to invoke")
    tool_input: dict = Field(description="The input to pass in to the Tool")


class OutputParserNoTools(Runnable):
    
    def __init__(self, response: BaseModel, **kwargs):
        super().__init__(**kwargs)
        self.response = response

    def invoke(self, data: dict, config):
        if data['parsing_error']:
            import instructor
            
            print('OutputParser')
            print('raw result:', data['raw'])
        
            # Extract structured data from natural language
            client = instructor.from_openai(OpenAI())
            message = {
                'content': data['raw'].content,
                'additional_kwargs': data['raw'].additional_kwargs 
            }
            res = client.chat.completions.create(
                model=os.environ.get("chat_model", "gpt-4o"),
                response_model=self.response,
                messages=[{"role": "user", "content": json.dumps(message)}],
            )
            print('instructor result:', res.dict())
        else:
            res = data['parsed']
        
        return res
        

class OutputParserWithTools(Runnable):
    def __init__(self, response: BaseModel, **kwargs):
        super().__init__(**kwargs)
        self.response = response

    def invoke(self, msg: AIMessage, config):
        #Chose only first tool_call
        tool_call = msg.tool_calls[0]
        
        if tool_call['name'] == 'final_answer':
            return self.response(**tool_call['args'])
        
        tool_data = {
            "tool_name": tool_call['name'], 
            "tool_input": tool_call['args']
            }
        
        return ToolMessage(**tool_data)
        

def agent_with_structured_output_factory(
        prompt: ChatPromptTemplate,
        llm: BaseLanguageModel,
        tools: List[StructuredTool],
        response_model: BaseModel
    ):
    
    if not tools:
        return prompt | llm.with_structured_output(response_model, include_raw=True) |  OutputParserNoTools(response_model)
    
    def dummy():
        pass
    
    final_answer = StructuredTool.from_function(
        func=dummy,
        name="final_answer",
        description= (
            "Use to send final answer to user"
        ),
        args_schema=response_model,
        return_direct=False
    )
    
    tools += [final_answer]
    
    if 'tools_list' in prompt.input_variables:
        #tools_list = custom_render_tools(tools)
        tools_list = custom_render_text_description_and_args(tools, short=False)
        prompt = prompt.partial(tools_list=tools_list)
    else:
        raise ValueError("tools_list not found in prompt")
    
    llm_with_tools = llm.bind_tools(tools=tools, tool_choice="any")
    agent = prompt| llm_with_tools |  OutputParserWithTools(response_model)
        
    return agent
