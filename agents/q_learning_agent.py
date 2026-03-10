### q_learning_agent.py
### Implements the QLearningAgent class

from agents.base_agent import BaseAgent
import random

class QLearningAgent(BaseAgent):
    def __init__(self, lr=0.1, discount_factor=0.9, mode="exploitation"):
        self.lr = lr
        self.df = discount_factor
        self.mode = mode
        self.qtable = {}

    def chose_action(self, grid):
        grid = tuple(grid)
        if self.mode == "exploitation":
            possible_actions = self.qtable[grid]
            action = max(possible_actions, key=possible_actions.get)
            return action
        if self.mode == "exploration":
            if grid in self.qtable:
                possible_actions = self.qtable[grid]
            else : 
                possible_actions = [i for i in range(9) if grid[i] is None]
            action = random.choice(list(possible_actions))
            return action

    def update_qtable(self, grid, action, reward, new_grid):
        #print("previous qtable : ", self.qtable)
        grid, new_grid = tuple(grid), tuple(new_grid)
        if grid not in self.qtable :
            #self.qtable[grid] = [0 if grid[i] is None else float('-inf') for i in range(9)]
            self.qtable[grid] = {i : 0 for i in range(9) if grid[i] is None}
        if new_grid not in self.qtable : 
            self.qtable[new_grid] = {i : 0 for i in range(9) if new_grid[i] is None}
        
        future_actions = self.qtable[new_grid]
        if future_actions :
            max_future_q = max(future_actions, key=future_actions.get)
        else : 
            max_future_q = 0
        Q_new = reward + self.df * max_future_q
        self.qtable[grid][action] += self.lr * (Q_new - self.qtable[grid][action])
        #print("new qtable : ", self.qtable)