from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
