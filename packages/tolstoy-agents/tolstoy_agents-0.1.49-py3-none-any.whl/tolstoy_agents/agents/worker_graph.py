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

import json
import functools
import operator
from langchain.schema import (
    AIMessage,
    HumanMessage
)
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import BaseMessage

from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_core.prompts import ChatPromptTemplate
from tolstoy_agents.agents import agent_with_structured_output_factory
from abc import ABC, abstractmethod
from langchain.tools import StructuredTool

class AgentState(TypedDict):
    output: BaseModel
    chat_history: list[BaseMessage]
    context_data: Optional[list[BaseModel]]
    agent_scratchpad: Annotated[Sequence[BaseMessage], operator.add]


class AbstractWorkerGraph(ABC):
    @abstractmethod
    def agent_logic(self, **kwargs):
        pass

    @abstractmethod
    def executor_logic(self, **kwargs):
        pass

    @abstractmethod
    def create_workflow(self, **kwargs):
        pass
        
    def invoke(self, **kwargs):
        return self.workflow.invoke(**kwargs)
    

class WorkerGraph(AbstractWorkerGraph):
    def __init__(self,
                 prompt,
                 llm,
                 internal_tools: List[StructuredTool],
                 external_tools: List[StructuredTool],
                 response: BaseModel):
        
        self.internal_tools = internal_tools
        self.external_tools = external_tools
        self.agent_runnable = agent_with_structured_output_factory(
            prompt,
            llm,
            internal_tools+external_tools,
            response
            )
        self.workflow = self.create_workflow()
    

    def agent_logic(self, state):
        if state.get('agent_scratchpad', None) is None:
           state['agent_scratchpad'] = []
        #===========================LLM===========================
        result = self.agent_runnable.invoke(state)
        #=========================================================

        return {"output": result}


    def executor_logic(self, state):
        internal_tools_map = {t.name: t for t in self.internal_tools}
        #external_tools_map = {t.name: t for t in self.external_tools}
        
        agent_output = state["output"]
        
        # if destination in external_tools_map:
        #     return {
        #         "destination": 'Tool',
        #         "message": {'action':message.tool_name, 'action_input': message.tool_input}
        #     }

        print(f'Invoking {agent_output.tool_name}')
        result = internal_tools_map[agent_output.tool_name].run(tool_input=agent_output.tool_input)

        return {
            "agent_scratchpad": [
                AIMessage(content=json.dumps({
                    "tool_name": agent_output.tool_name,
                    "tool_input": agent_output.tool_input
                }), name='Worker'),
                AIMessage(content=str(result), name=f"{agent_output.tool_name}_Tool")
            ]
        }


    def create_workflow(self):
        workflow = StateGraph(AgentState)
        
        #================NODES================
        workflow.add_node("Agent", self.agent_logic)
        workflow.add_node("Executor", self.executor_logic)
        
        workflow.set_entry_point('Agent')

        #================EDGES================
        def next_step(state):
            output = state['output']
            
            try:
                tool_name = output.tool_name
            except:
                #if no tool_name, then it is a message for user
                return END
            
            if tool_name in ['ask_human', 'ask_internal_support']:
                return END
            
            return "Executor"

        workflow.add_conditional_edges("Agent", next_step)
        workflow.add_edge("Executor", "Agent")

        graph = workflow.compile()
        
        return graph
