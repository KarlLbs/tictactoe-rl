### middle_random_agent.py
### Implements the MiddleRandomAgent class, an agent that plays in the middle square and then randomly

from agents.base_agent import BaseAgent
import random

class MiddleRandomAgent(BaseAgent):
    def __init__(self):
        pass

    def chose_action(self, grid):
        available_squares = [i for i in range(9) if grid[i]==None]
        if 4 in available_squares:
            return 4
        elif available_squares != []:
            return random.choice(available_squares)