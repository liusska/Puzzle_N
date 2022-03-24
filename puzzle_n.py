import random

from boards import Board


class Game:
    def __init__(self, board):
        self.board = board

    def move_target_cell(self, direction):
        pass

    def check_is_the_puzzle_solved(self):
        pass


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


if __name__ == '__main__':
    main()


