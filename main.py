### main.py

from game import Game

def main2():
    game = Game()
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

if __name__ == "__main__":
    main2()
