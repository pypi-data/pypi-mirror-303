from abc import ABC, abstractmethod
from tolstoy_agents.utils import get_langsmith_url

class Executor(ABC):
    @abstractmethod
    def __init__(self, context: dict)->None:
        pass
    
    def run(self, context: dict)->dict:
        from langchain.callbacks import collect_runs

        with collect_runs() as cb:
            result = self.workflow.invoke(context)
            result['langsmith_url'] = get_langsmith_url(cb)
            
        return result