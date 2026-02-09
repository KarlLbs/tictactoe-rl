### random_agent.py
### Implements the RandomAgent class, an agent that plays randomly

from base_agent import BaseAgent
import numpy as np
import random

class RandomAgent(BaseAgent):
    def __init__(self):
        pass

    def chose_action(self, grid):
        available_squares = [i for i in range(9) if grid[i]==None]
        if available_squares != []:
            return random.choice(available_squares)