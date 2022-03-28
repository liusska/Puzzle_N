import random

from boards import Board


def main():
    board = Board(4)
    board.shuffle_board()
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
        if board.check_is_the_puzzle_solved(board):
            print("The puzzle is solved!")
            break


if __name__ == '__main__':
    main()
