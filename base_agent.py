### base_agent.py
### Implements the BaseAgent class, an abstract class for all agents

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def chose_action(self, observation)->int:
        pass