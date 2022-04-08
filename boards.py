import copy
import random
import inspect


class Board:
    """
    This class controls the puzzle board and the operations related with the board.
    """
    EMPTY_CELL = ' '
    START_NUMBER = 0
    SHUFFLE_COUNT = 1000

    def __init__(self, side):
        self.side = side
        self.fields_count = side * side
        self.board = self.initialize_sorted_board()
        self.winning_board = copy.deepcopy(self.board)
        self.possible_moves = [method for method_name, method
                               in inspect.getmembers(self, predicate=inspect.ismethod)
                               if method_name.startswith('move_')]

    def create_board_for_test(self, new_state):
        """
        Set a board 4x4 with 3 moves left for puzzle solved state:
        The steps for win are:
            1.move: down
            2.move: right
            3.move: right
        This is used for quick puzzle tests.
        """
        self.board = copy.deepcopy(new_state)
        return self.board

    def number_generator(self):
        """
        Generate numbers, in range (1, side * side) that will be set to the
        board initialization.
        """
        self.START_NUMBER += 1
        return self.START_NUMBER

    def initialize_sorted_board(self):
        """
        Initialize sorted started state of the game board.
        Set the last cell of the board to an EMPTY CELL
        """
        board = self.generate_board()
        board[self.side-1][self.side-1] = self.EMPTY_CELL
        return board

    def generate_board(self):
        """
        Returns the board cells in nested array with dimensions side * side.
        """
        board = []
        for r in range(self.side):
            row = []
            for c in range(self.side):
                row.append(self.number_generator())
            board.append(row)
        return board

    def shuffle_board(self):
        """
         Mix the board cells with random chosen move from list with all type of moves.
         The operation repeats SHUFFLE_COUNT times.
        """
        for _ in range(self.SHUFFLE_COUNT):
            random.choice(self.possible_moves)()

    def find_target_cell(self, searched_value, board):
        """
        Search cell by cell for the EMPTY_CELL which is the target cell.
        """
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if board[r][c] == searched_value:
                    return r, c

    def is_valid_move(self, row, col):
        """
        Returns True if the coordinates of the current move are in the board range.
        """
        return 0 <= row < self.side and 0 <= col < self.side

    def abstract_move(self, delta_row, delta_col):
        """
        Make the user move based on the given coordinates if they are valid.
        Swap the element and the EMPTY CELL after validation.
        """
        row, col = self.find_target_cell(self.EMPTY_CELL, self.board)
        valid_coordinates = self.is_valid_move(row + delta_row, col + delta_col)
        if valid_coordinates:
            element = self.make_move(row + delta_row, col + delta_col)
            self.board[row][col] = element

    def move_left(self):
        """
        Call the abstract_move func with correct for the left move coordinates.
        """
        self.abstract_move(0, -1)

    def move_right(self):
        """
        Call the abstract_move func with correct for the right move coordinates.
        """
        self.abstract_move(0, +1)

    def move_up(self):
        """
        Call the abstract_move func with correct for the up move coordinates.
        """
        self.abstract_move(-1, 0)

    def move_down(self):
        """
        Call the abstract_move func with correct for the down move coordinates.
        """
        self.abstract_move(+1, 0)

    def make_move(self, target_row, target_col):
        """
        Set the new cell with EMPTY_CELL value.
        Returns the previous element.
        """
        element = self.board[target_row][target_col]
        self.board[target_row][target_col] = self.EMPTY_CELL
        return element

    def __str__(self):
        """
        Returns a string representation of the board state in understandable
        for player form.
        """
        result = ''
        for row in range(self.side):
            for col in range(self.side):
                result += str(self.board[row][col]) + ' '
                if self.board[row][col] == self.EMPTY_CELL or self.board[row][col] < 10:
                    result += ' '
            result += '\n'
        return result

