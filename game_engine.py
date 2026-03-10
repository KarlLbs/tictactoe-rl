### game_engine.py
### Implements the GameEngine class, to run games

class GameEngine():
    def __init__(self, gameState, player1, player2):
        self.state = gameState
        self.player1 = player1
        self.player2 = player2

    def play_game(self, render=False):
        grid = self.state.reset()
        done_flag = False
        while not done_flag:
            if self.state.whos_turn_is_it()==1:
                move = self.player1.chose_action(grid)
                grid, done_flag = self.state.step(move)
                if render : 
                    print(f"Player 1 move : square {move}")
                    self.state.render()
            else : 
                move = self.player2.chose_action(grid)
                grid, done_flag = self.state.step(move)
                if render : 
                    print(f"Player 2 move : square {move}")
                    self.state.render()
        if self.state.detect_end()==0:
            if render : 
                print("Tie !")
                self.state.render()
            return 0
        else : 
            winner = 1 if self.state.whos_turn_is_it()==2 else 2
            if render : 
                print(f"Player {winner} victory !")
            return winner
    
    def play_x_games(self, x:int, render=False):
        wins = []
        for _ in range(x):
            wins.append(self.play_game(render))
        print(f"Results after {x} games :")
        print(f"Player 1 ({self.player1.__repr__()}): {wins.count(1)} wins ({100*wins.count(1)/len(wins):.2f}%)")
        print(f"Player 2 ({self.player2.__repr__()}): {wins.count(2)} wins ({100*wins.count(2)/len(wins):.2f}%)")
        print(f"Ties : {wins.count(0)} ({100*wins.count(0)/len(wins):.2f}%)")
    
    def play_x_games_fair(self, x:int, render=False):
        wins = []
        for _ in range(x//2):
            wins.append(self.play_game(render))
        self.__init__(self.state, self.player2, self.player1)
        for _ in range(x//2 + x%2):
            winner = 1 if self.play_game(render)==2 else 2
            wins.append(winner)
        print(f"Results after {x} games, alternating who starts:")
        print(f"{self.player2.__repr__()}: {wins.count(1)} wins ({100*wins.count(1)/len(wins):.2f}%)")
        print(f"{self.player1.__repr__()}: {wins.count(2)} wins ({100*wins.count(2)/len(wins):.2f}%)")
        print(f"Ties : {wins.count(0)} ({100*wins.count(0)/len(wins):.2f}%)")  
