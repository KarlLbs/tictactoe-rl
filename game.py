### game.py
### Implements the Game class

class Game:
    def __init__(self):
        self.grid = [0 for _ in range(9)]
        self.player = 1

    def reset(self):
        self.__init__()

    def detect_end(self):
        a = (self.grid[0]==self.grid[1]==self.grid[2] and self.grid[0]!=0)
        b = (self.grid[3]==self.grid[4]==self.grid[5] and self.grid[3]!=0)
        c = (self.grid[6]==self.grid[7]==self.grid[8] and self.grid[6]!=0)
        d = (self.grid[0]==self.grid[3]==self.grid[6] and self.grid[0]!=0)
        e = (self.grid[1]==self.grid[4]==self.grid[7] and self.grid[1]!=0)
        f = (self.grid[2]==self.grid[5]==self.grid[8] and self.grid[2]!=0)
        g = (self.grid[0]==self.grid[4]==self.grid[8] and self.grid[0]!=0)
        h = (self.grid[2]==self.grid[4]==self.grid[6] and self.grid[2]!=0)
        if a or b or c or d or e or f or g or h : 
            return True

    def check_action(self, square, player):
        if self.detect_end():
            raise ValueError("The game is already over !")
        if player != self.player:
            raise ValueError(f"It's not player {player}'s turn !")
        if self.grid[square] != 0:
            raise ValueError(f"Square {square} has already been filled !")


    def step(self, square, player):
        try :
            self.check_action(square, player)
        except Exception as e : 
            print("Invalid move : ", e)
            return
        self.grid[square] = 1 if player==1 else -1
        if self.detect_end() : 
            print(f"Player {player} victory !")
            return
        self.player = 2 if player==1 else 1

    def render(self):
        grid2 = [' ' if i==0 else i for i in self.grid]
        grid2 = ['X' if i==1 else i for i in grid2]
        grid2 = ['O' if i==-1 else i for i in grid2]
        print("Current state of the game :")
        print(" --- --- --- ")
        print(f"| {grid2[0]} | {grid2[1]} | {grid2[2]} |")
        print(" --- --- --- ")
        print(f"| {grid2[3]} | {grid2[4]} | {grid2[5]} |")
        print(" --- --- --- ")
        print(f"| {grid2[6]} | {grid2[7]} | {grid2[8]} |")
        print(" --- --- --- ")