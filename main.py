### main.py

from training import Trainer
from game_state import GameState
from game_engine import GameEngine
from agents.human_agent import HumanAgent
from agents.random_agent import RandomAgent
from agents.q_learning_agent import QLearningAgent
from agents.next_square_agent import NextSquareAgent
from agents.middle_random_agent import MiddleRandomAgent
from agents.deep_learning_agent import DeepLearningAgent
from tests import test_game_state, test_random_agent, test_engine, test_tournament

def main():
    game = GameState()
    agent = QLearningAgent(mode="exploration")
    opponent = RandomAgent()

    # Before training
    print("Before training :")
    engine = GameEngine(game, agent, opponent)
    engine2 = GameEngine(game, opponent, agent)
    engine.play_x_games(10000)
    engine2.play_x_games(10000)

    # Training
    nb_episodes = 10000
    trainer = Trainer(game)
    trainer.qlearning_training_loop(nb_episodes, agent, opponent)

    #print(agent.qtable[tuple([None for _ in range(9)])])

    # After training
    print("\nAfter training :")
    agent.mode = "exploitation"
    engine.play_x_games(10000)
    engine2.play_x_games(10000)

if __name__ == "__main__":
    main()