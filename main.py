### main.py

from game_state import GameState
from random_agent import RandomAgent

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

def main():
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

if __name__ == "__main__":
    main()
