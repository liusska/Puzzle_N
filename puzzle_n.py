from boards import Board
from puzzleN.game import Game


def main():
    board = Board(2)
    board.shuffle_board()
    game = Game()
    print(board)

    while True:
        print('Enter move: ')
        direction = input().split()
        for action in direction:
            if action == 'w':
                board.move_up()
            elif action == 's':
                board.move_down()
            elif action == 'a':
                board.move_left()
            elif action == 'd':
                board.move_right()

        print(board)

        if game.check_is_the_puzzle_solved(board.board):
            print("*** The puzzle is SOLVED! ***")
            break


if __name__ == '__main__':
    main()
