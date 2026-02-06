### game.py
### Implements the Game class

class Game2:
    def __init__(self):
        self.grid = [None for _ in range(9)]

    def reset(self):
        self.__init__()

    def detect_end(self):
        """a = abs(self.grid[0] + self.grid[1] + self.grid[2])==3
        b = abs(self.grid[3] + self.grid[4] + self.grid[5])==3
        c = abs(self.grid[6] + self.grid[7] + self.grid[8])==3
        d = abs(self.grid[0] + self.grid[3] + self.grid[6])==3
        e = abs(self.grid[1] + self.grid[4] + self.grid[7])==3
        f = abs(self.grid[2] + self.grid[5] + self.grid[8])==3
        g = abs(self.grid[0] + self.grid[4] + self.grid[8])==3
        h = abs(self.grid[2] + self.grid[4] + self.grid[6])==3"""
        a = (self.grid[0]==self.grid[1]==self.grid[2] and self.grid[0])
        b = (self.grid[3]==self.grid[4]==self.grid[5] and self.grid[3])
        c = (self.grid[6]==self.grid[7]==self.grid[8] and self.grid[6])
        d = (self.grid[0]==self.grid[3]==self.grid[6] and self.grid[0])
        e = (self.grid[1]==self.grid[4]==self.grid[7] and self.grid[1])
        f = (self.grid[2]==self.grid[5]==self.grid[8] and self.grid[2])
        g = (self.grid[0]==self.grid[4]==self.grid[8] and self.grid[0])
        h = (self.grid[2]==self.grid[4]==self.grid[6] and self.grid[2])
        if a or b or c or d or e or f or g or h : 
            return True

    def whos_turn_is_it(self):
        if len([i for i in self.grid if i])%2 == 0:
            return 1
        else :
            return 2

    def check_action(self, square):
        if self.detect_end():
            raise ValueError("The game is already over !")
        if self.grid[square] :
            raise ValueError(f"Square {square} has already been filled !")


    def step(self, square):
        try :
            self.check_action(square)
        except Exception as e : 
            print("Invalid move : ", e)
            return
        player = self.whos_turn_is_it()
        self.grid[square] = 1 if player==1 else -1
        if self.detect_end() : 
            print(f"Player {player} victory !")
            return

    def render(self):
        grid2 = [' ' if i==None else i for i in self.grid]
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


