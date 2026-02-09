### human_agent.py
### Implements the HumanAgent class, an agent to play through the terminal

from base_agent import BaseAgent

class HumanAgent(BaseAgent):
    def __init__(self):
        pass

    def chose_action(self, observation):
        action = input("Enter the square you want to play in : ")
        return int(action)