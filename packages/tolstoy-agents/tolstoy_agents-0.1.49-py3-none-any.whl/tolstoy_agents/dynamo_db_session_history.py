from typing import Optional, Type, List
from botocore.exceptions import ClientError
from pydantic import Field
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory

class DevDynamoDBChatMessageHistory(DynamoDBChatMessageHistory):
    """Ability to add any json to Dynamo."""
    callbacks: List[callable] = Field([], description=(
            "Functions to call when updating."
        ))
    
    def __init__(self, table_name, session_id, callbacks: List[callable]=[]):
        self.callbacks = callbacks
        super().__init__(table_name, session_id)
        
        
    @property
    def item(self) -> str:
        response = self.table.get_item(Key=self.key)

        if response and "Item" in response:
            return response["Item"]

        return {} 
        
    @property
    def parent_session(self) -> str:
        response = self.table.get_item(Key=self.key)
        return self.item.get('parent_session', '')

    #state of communication direction
    @property
    def state(self) -> str:
        response = self.table.get_item(Key=self.key)
        return self.item.get('state', '')
    
    #task under which the session is working
    @property
    def objective(self) -> str:
        response = self.table.get_item(Key=self.key)
        return self.item.get('objective', '')
    
    #state of manager
    @property
    def title(self) -> str:
        response = self.table.get_item(Key=self.key)
        return self.item.get('title', '')
    
    @property
    def high_level_reasoning(self) -> str:
        response = self.table.get_item(Key=self.key)
        return self.item.get('high_level_reasoning', '')

    @property
    def low_level_steps(self) -> List[str]:
        response = self.table.get_item(Key=self.key)
        return self.item.get('low_level_steps', [])
    
    @property
    def preliminary_plan(self) -> List[str]:
        response = self.table.get_item(Key=self.key)
        return self.item.get('preliminary_plan', [])
    
    @property
    def high_level_plan(self) -> List[str]:
        response = self.table.get_item(Key=self.key)
        return self.item.get('high_level_plan', [])
    
    @property
    def high_level_assumptions(self) -> List[str]:
        response = self.table.get_item(Key=self.key)
        return self.item.get('high_level_assumptions', [])
    
    @property
    def messages_for_planner(self) -> List[dict]:
        response = self.table.get_item(Key=self.key)
        return self.item.get('messages_for_planner', [])

    @property
    def messages_for_manager(self) -> List[dict]:
        """Retrieve the messages from DynamoDB"""
        response = self.table.get_item(Key=self.key)
        return self.item.get('messages_for_manager', [])

    @property
    def messages_for_worker(self) -> List[dict]:
        """Retrieve the messages from DynamoDB"""
        response = self.table.get_item(Key=self.key)
        return self.item.get('messages_for_worker', [])

    @property
    def done_steps(self) -> dict:
        """Retrieve the messages from DynamoDB"""
        response = self.table.get_item(Key=self.key)
        return self.item.get('done_steps', [])
    
    @property
    def artifacts(self) -> List[str]:
        """Retrieve the messages from DynamoDB"""
        response = self.table.get_item(Key=self.key)
        return self.item.get('artifacts', {})

    # functions
    def update_objective(self, objective: str) -> None:
        """Append the item to the record in DynamoDB"""
        data=self.item
        data['objective'] = objective
        self.put_item(data)
    
    def put_item(self, data: dict) -> None:    
        try:
            if self.ttl:
                import time

                expireAt = int(time.time()) + self.ttl
                self.table.put_item(
                    Item={
                        **self.key,
                        **data,
                        self.ttl_key_name: expireAt
                    }
                )
            else:
                self.table.put_item(
                    Item={
                        **self.key,
                        **data
                    }
                    )
        except ClientError as err:
            print(err)
            
    def update_low_level_steps(self, low_level_steps: List[str]) -> None:
        """Append the item to the record in DynamoDB"""
        data=self.item
        data['low_level_steps'] = low_level_steps
        self.put_item(data)
            
    def update_preliminary_plan(self, steps: List[str]) -> None:
        data=self.item
        data['preliminary_plan'] = steps
        self.put_item(data)
        
    def update_high_level_plan(self, steps: List[str]) -> None:
        data=self.item
        data['high_level_plan'] = steps
        self.put_item(data)
        
    def update_high_level_assumptions(self, assumptions: List[str]) -> None:
        data=self.item
        data['high_level_assumptions'] = assumptions
        self.put_item(data)
        
    def update_state(self, state: str) -> None:
        data=self.item
        data['state'] = state
        self.put_item(data)
        
    def update_high_level_reasoning(self, reasoning: str) -> None:
        data=self.item
        data['high_level_reasoning'] = reasoning
        self.put_item(data)
            
    def update_title(self, title: str) -> None:
        data=self.item
        data['title'] = title
        self.put_item(data)
            
    def update_parent_session(self, parent_session: str) -> None:
        """Append the item to the record in DynamoDB"""
        data=self.item
        data['parent_session'] = parent_session
        self.put_item(data)

    def add_done_step(self, high_level_step: str, low_level_step: str, result: str) -> None:
        """Append the item to the record in DynamoDB"""
        data = self.item
        done_steps = self.done_steps
        done_steps.append((high_level_step, low_level_step, result))
        data['done_steps'] = done_steps
        self.put_item(data)
        
    def add_artifact(self, key: str, value: str) -> None:
        """Append the item to the record in DynamoDB"""
        data=self.item
        artifacts = self.artifacts
        artifacts[key] = value
        data['artifacts'] = artifacts
        self.put_item(data)

    def add_message(self, msg: dict, destination: str) -> None:
        """Append the message to the record in DynamoDB"""
        data=self.item
        
        if destination=='Manager':
            messages = self.messages_for_manager
            messages.append(msg)
            data['messages_for_manager'] = messages
        elif destination=='Planner':
            messages = self.messages_for_planner
            messages.append(msg)
            data['messages_for_planner'] = messages
        elif destination=='Worker':
            messages = self.messages_for_worker
            messages.append(msg)
            data['messages_for_worker'] = messages

        for callback in self.callbacks:
            callback({
                "message": msg['message'],
                "source": msg['source'],
                "destination": msg['destination'],
                "title": self.title
                })

        self.put_item(data)

    def clear(self, destination=None) -> None:
        """Clear session memory from DynamoDB"""
        if not destination:
            try:
                self.table.delete_item(Key=self.key)
            except ClientError as err:
                print(err)

            return

        data=self.item
        if destination=='Worker':
            data['messages_for_worker'] = []
        elif destination=='Planner':
            data['messages_for_planner'] = []

        self.put_item(data)


def next_plan(session_history: DevDynamoDBChatMessageHistory):
    message = ''

    if session_history.low_level_steps[1:]:
        prev_plan=''
        for _, step in enumerate(session_history.low_level_steps[1:]):
            prev_plan+=f'- {step}\n'
        message = prev_plan

    return


def get_done_steps(session_history: DevDynamoDBChatMessageHistory):
    message = ''

    if session_history.done_steps:
        done_steps = session_history.done_steps
        
        for ix, data in enumerate(done_steps):
            k,g,r = data
            message += f"- ID: {ix+1}\n"
            message += f"- Title: {g}\n"
            message += f"- Context: {r}\n\n"

    return message