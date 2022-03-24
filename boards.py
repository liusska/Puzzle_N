import random
import inspect


class Board:
    EMPTY_CELL = ' '
    START_NUMBER = 0
    SHUFFLE_COUNT = 1000

    def __init__(self, side):
        self.side = side
        self.fields_count = side * side
        self.board = self.initialize_sorted_board()
        self.possible_moves = [method for method_name, method
                               in inspect.getmembers(self, predicate=inspect.ismethod)
                               if method_name.startswith('move_')]

    def number_generator(self):
        self.START_NUMBER += 1
        return self.START_NUMBER

    def initialize_sorted_board(self):
        board = self.generate_board()
        board[self.side-1][self.side-1] = self.EMPTY_CELL
        return board

    def generate_board(self):
        board = []
        for r in range(self.side):
            row = []
            for c in range(self.side):
                row.append(self.number_generator())
            board.append(row)
        return board

    def find_target_cell(self):
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c] == self.EMPTY_CELL:
                    return r, c

    def is_valid_move(self, row, col):
        return 0 <= row < self.side and 0 <= col < self.side

    def move_left(self):
        row, col = self.find_target_cell()
        valid_coordinates = self.is_valid_move(row, col - 1)
        if valid_coordinates:
            element = self.make_move(row, col - 1)
            self.board[row][col] = element

    def move_right(self):
        row, col = self.find_target_cell()
        valid_coordinates = self.is_valid_move(row, col + 1)
        if valid_coordinates:
            element = self.make_move(row, col + 1)
            self.board[row][col] = element

    def move_up(self):
        row, col = self.find_target_cell()
        valid_coordinates = self.is_valid_move(row - 1, col)
        if valid_coordinates:
            element = self.make_move(row - 1, col)
            self.board[row][col] = element

    def move_down(self):
        row, col = self.find_target_cell()
        valid_coordinates = self.is_valid_move(row + 1, col)
        if valid_coordinates:
            element = self.make_move(row + 1, col)
            self.board[row][col] = element

    def make_move(self, target_row, target_col):
        element = self.board[target_row][target_col]
        self.board[target_row][target_col] = self.EMPTY_CELL
        return element

    def shuffle_board(self):
        for _ in range(self.SHUFFLE_COUNT):
            random.choice(self.possible_moves)()

    def __str__(self):
        result = ''
        for row in range(self.side):
            for col in range(self.side):
                result += str(self.board[row][col]) + ' '
                if self.board[row][col] == self.EMPTY_CELL or self.board[row][col] < 10:
                    result += ' '
            result += '\n'
        return result

