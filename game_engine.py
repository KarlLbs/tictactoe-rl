### game_engine.py
### Implements the GameEngine class, to run games

class GameEngine():
    def __init__(self, gameState, player1, player2):
        self.state = gameState
        self.player1 = player1
        self.player2 = player2

    def play_game(self, render=False):
        self.state.reset()
        while self.state.detect_end()==-1:
            grid = self.state.grid
            if self.state.whos_turn_is_it()==1:
                move = self.player1.chose_action(grid)
                self.state.step(move)
                if render : 
                    print(f"Player 1 move : square {move}")
                    self.state.render()
            else : 
                move = self.player2.chose_action(grid)
                self.state.step(move)
                if render : 
                    print(f"Player 2 move : square {move}")
                    self.state.render()
        if self.state.detect_end()==0:
            return 0
        return 1 if self.state.whos_turn_is_it()==2 else 2
    
    def play_x_games(self, x:int, render=False):
        wins = []
        for _ in range(x):
            wins.append(self.play_game(render))
        print(f"Results after {x} games :")
        print(f"Player 1 : {wins.count(1)} wins ({100*wins.count(1)/len(wins)}%)")
        print(f"Player 2 : {wins.count(2)} wins ({100*wins.count(2)/len(wins)}%)")
        print(f"Ties : {wins.count(0)} ({100*wins.count(0)/len(wins)}%)")
