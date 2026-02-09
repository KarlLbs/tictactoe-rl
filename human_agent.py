### human_agent.py
### Implements the HumanAgent class, an agent to play through the terminal

from base_agent import BaseAgent

class HumanAgent(BaseAgent):
    def __init__(self):
        pass

    def chose_action(self, observation):
        while True : 
            action = input("Enter the square you want to play in : ")
            try : 
                value = int(action)
                if value<0 or value>8:
                    print("Please input a square number between 0 and 8 included.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid square integer.")