from puzzleN.boards import Board


class Game:
    """
    This class controls the user moves in the current game.
    """

    def play(self):
        """
        Set a new board for the puzzle game.
        Controls the moves until the puzzle is solved.
        """
        board = Board(4)
        board.shuffle_board()
        print(board)

        while not self.check_if_the_puzzle_is_solved(board.board):
            self.solve_the_puzzle_step(board)

    def solve_the_puzzle_step(self, board):
        """
        Take the user input (one or more) for up, down, left or right and
        call the control_the_input_actions with the given from user params
        """
        print('Enter move: ')
        self.control_the_actions(board, input())
        print(board)

    @staticmethod
    def control_the_actions(board, directions):
        """
        Make the user action depends on the given directions.
        """
        for action in directions:
            if action == 'w':
                board.move_up()
            elif action == 's':
                board.move_down()
            elif action == 'a':
                board.move_left()
            elif action == 'd':
                board.move_right()

    @staticmethod
    def check_if_the_puzzle_is_solved(board):
        """
        Check if the current puzzle state is equal to solved puzzle state.
        If is - prints a message and the game is over.
        """

        solved_board_state = Board(len(board)).winning_board
        current_board_state = board
        if solved_board_state == current_board_state:
            print("*** The puzzle is SOLVED! ***")
            return True
        return False

