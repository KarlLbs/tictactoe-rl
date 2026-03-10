### q_learning_agent.py
### Implements the QLearningAgent class

from agents.base_agent import BaseAgent
import random

class QLearningAgent(BaseAgent):
    def __init__(self, lr=0.1, discount_factor=0.9, mode="exploitation"):
        self.lr = lr
        self.df = discount_factor
        self.mode = mode
        self.qtable = [] ##### TODO : Design the Q-table

    def chose_action(self, state):
        if self.mode == "exploitation":
            possible_actions = self.qtable(state)
            action = max(possible_actions)
            return possible_actions.index(action)
        if self.mode == "exploration":
            possible_actions = self.qtable(state)
            action = random.choice(possible_actions)
            return possible_actions.index(action)

    def update_qtable(self, state, action, reward, new_state):
        Q_new = reward + self.df * max(self.qtable(new_state))
        self.qtable(state)[action] = (1-self.lr) * self.qtable(state)[action] + self.lr * Q_new