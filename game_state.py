### game_state.py
### Implements the GameState class

class GameState:
    def __init__(self):
        self.grid = [None for _ in range(9)]

    def reset(self):
        self.__init__()
        return self.grid

    def detect_end(self):
        a = (self.grid[0]==self.grid[1]==self.grid[2] and self.grid[0])
        b = (self.grid[3]==self.grid[4]==self.grid[5] and self.grid[3])
        c = (self.grid[6]==self.grid[7]==self.grid[8] and self.grid[6])
        d = (self.grid[0]==self.grid[3]==self.grid[6] and self.grid[0])
        e = (self.grid[1]==self.grid[4]==self.grid[7] and self.grid[1])
        f = (self.grid[2]==self.grid[5]==self.grid[8] and self.grid[2])
        g = (self.grid[0]==self.grid[4]==self.grid[8] and self.grid[0])
        h = (self.grid[2]==self.grid[4]==self.grid[6] and self.grid[2])
        i = (self.grid.count(None)==0)
        if a or b or c or d or e or f or g or h: 
            return 1 # Win (winner determined by who last played)
        elif i :
            return 0 # No win but full grid : tie
        else : 
            return -1

    def whos_turn_is_it(self):
        if len([i for i in self.grid if i])%2 == 0:
            return 1
        else :
            return 2

    def check_action(self, square):
        if self.detect_end()==1 or self.detect_end()==0:
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
        done_flag = (self.detect_end() != -1)
        return self.grid, done_flag

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


