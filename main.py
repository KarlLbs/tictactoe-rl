### main.py

from game_state import GameState
from game_engine import GameEngine
from agents.human_agent import HumanAgent
from agents.random_agent import RandomAgent
from agents.next_square_agent import NextSquareAgent


def game_state():
    game = GameState()
    game.render()
    game.step(4)
    game.render()
    game.step(0)
    game.render()
    game.step(1)
    game.render()
    game.step(2)
    game.render()
    game.step(1)
    game.render()
    game.step(6)
    game.render()
    game.step(8)
    game.render()
    game.step(7)
    game.render()
    game.step(4)
    game.reset()
    game.render()

def random_agent():
    game = GameState()
    agent1 = RandomAgent()
    agent2 = RandomAgent()
    while not game.detect_end():
        grid = game.grid
        game.step(agent1.chose_action(grid))
        game.render()
        grid = game.grid
        game.step(agent2.chose_action(grid))
        game.render()

def main():
    engine = GameEngine(GameState(), RandomAgent(), NextSquareAgent())
    engine.play_x_games(10000)
    engine = GameEngine(GameState(), NextSquareAgent(), RandomAgent())
    engine.play_x_games(10000)
    engine.play_x_games_fair(10000)

if __name__ == "__main__":
    main()
