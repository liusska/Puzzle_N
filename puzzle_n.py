from puzzleN.boards import Board
from puzzleN.game import Game


def main():
    game = Game()
    board = Board(4)
    board.shuffle_board()
    # board.create_board_for_test()

    print(board)

    while not game.check_if_the_puzzle_is_solved(board.board):
        game.solve_the_puzzle(board, game)


if __name__ == '__main__':
    main()
