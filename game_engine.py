### game_engine.py
### Implements the GameEngine class, to run games

class GameEngine():
    def __init__(self, gameState, player1, player2):
        self.state = gameState
        self.player1 = player1
        self.player2 = player2

    def play_game(self, render=False):
        self.state.reset()
        while not self.state.detect_end():
            grid = self.state.grid
            if self.state.whos_turn_is_it()==1:
                move = self.player1.chose_action(grid)
                self.state.step(move)
                if render : 
                    self.state.render()
            else : 
                move = self.player2.chose_action(grid)
                self.state.step(move)
                if render : 
                    self.state.render()
        
