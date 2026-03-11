### main.py

from game_state import GameState
from game_engine import GameEngine
from agents.human_agent import HumanAgent
from agents.random_agent import RandomAgent
from agents.q_learning_agent import QLearningAgent
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
    while game.detect_end()==-1:
        grid = game.grid
        game.step(agent1.chose_action(grid))
        game.render()
        grid = game.grid
        game.step(agent2.chose_action(grid))
        game.render()

def game_engine():
    engine = GameEngine(GameState(), RandomAgent(), NextSquareAgent())
    engine.play_x_games(10000)
    engine = GameEngine(GameState(), NextSquareAgent(), RandomAgent())
    engine.play_x_games(10000)
    engine.play_x_games_fair(10000)

def training_loop():
    game = GameState()
    agent = QLearningAgent(mode="exploration")
    opponent = RandomAgent()

    # Before training
    print("Before training :")
    engine = GameEngine(game, agent, opponent)
    engine2 = GameEngine(game, opponent, agent)
    engine.play_x_games(10000)
    engine2.play_x_games(10000)

    nb_episodes = 50000
    for _ in range(nb_episodes):
        grid = game.reset()
        done_flag = False
        while not done_flag:
            # Playing turns
            action = agent.chose_action(grid)
            new_grid, done_flag = game.step(action)
            #game.render()
            if not done_flag : 
                new_grid, done_flag = game.step(opponent.chose_action(new_grid))
                #game.render()
            # Reward calculation and Q-table update
            if game.detect_end()==1 : # A player has won
                reward = 10 if game.whos_turn_is_it()==2 else -10
                agent.update_qtable(grid, action, reward, None)
            elif game.detect_end()==0 : # Tie
                reward = 0
                agent.update_qtable(grid, action, reward, None)
            else : # Game not over
                reward = 0 
                agent.update_qtable(grid, action, reward, new_grid)
            grid = new_grid

    #print(agent.qtable[tuple([None for _ in range(9)])])

    # After training
    print("\nAfter training :")
    agent.mode = "exploitation"
    engine.play_x_games(10000)
    engine2.play_x_games(10000)

if __name__ == "__main__":
    training_loop()
