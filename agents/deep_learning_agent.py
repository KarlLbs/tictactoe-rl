### deep_learning_agent.py
### Implements the DeepLearningAgent class

from agents.base_agent import BaseAgent
from sklearn.neural_network import MLPClassifier

class DeepLearningAgent(BaseAgent):
    def __init__(self, lr=0.1):
        self.lr = lr
        self.model = MLPClassifier()

    def chose_action(self, grid):
        return self.model.predict(grid)

    def train(self, grid, expected_move):
        self.model.fit(grid, expected_move)
