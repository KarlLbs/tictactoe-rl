from game import Game


def main():
    print("Hello from tictactoe-rl!")
    game = Game()
    game.render()
    game.step(4, 1)
    game.render()
    game.step(0, 2)
    game.render()
    game.step(1, 2)
    game.step(0, 1)
    game.render()
    game.step(2, 1)
    game.render()
    game.step(1, 2)
    game.render()
    game.step(6, 1)
    game.render()
    game.step(8, 2)
    game.reset()
    game.render()


if __name__ == "__main__":
    main()
