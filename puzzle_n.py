from puzzleN.boards import Board
from puzzleN.game import Game


def main():
    game = Game()
    board = game.set_new_game()
    # game.user_play(board)
    game.ai_play(board)


if __name__ == '__main__':
    main()
