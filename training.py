### training.py
### Implements the Trainer class, which provides the tools to train learning agents

from agents import q_learning_agent

class Trainer():
    def __init__(self, gameState) -> None:
        self.state = gameState

    def qlearning_training_loop(self, nb_episodes:int, agent:q_learning_agent, opponent):
        for _ in range(nb_episodes):
            grid = self.state.reset()
            done_flag = False
            while not done_flag:
                # Playing turns
                action = agent.chose_action(grid)
                new_grid, done_flag = self.state.step(action)
                #self.state.render()
                if not done_flag : 
                    new_grid, done_flag = self.state.step(opponent.chose_action(new_grid))
                    #self.state.render()
                # Reward calculation and Q-table update
                if self.state.detect_end()==1 : # A player has won
                    reward = 10 if self.state.whos_turn_is_it()==2 else -10
                    agent.update_qtable(grid, action, reward, None)
                elif self.state.detect_end()==0 : # Tie
                    reward = 0
                    agent.update_qtable(grid, action, reward, None)
                else : # Game not over
                    reward = 0 
                    agent.update_qtable(grid, action, reward, new_grid)
                grid = new_grid