### newt_square_agent.py
### Implements the NextSquareAgent class, an agent that plays in the next available square

from agents.base_agent import BaseAgent
import random

class NextSquareAgent(BaseAgent):
    def __init__(self):
        pass

    def chose_action(self, grid):
        available_squares = [i for i in range(9) if grid[i]==None]
        if available_squares != []:
            return available_squares[0]