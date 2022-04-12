from puzzleN.boards import Board
import ai_game


class Game:
    """
    This class controls the user moves in the current game.
    """

    @staticmethod
    def set_new_game():
        """
        Set a new board for the puzzle game.
        """
        board = Board(10)
        board.shuffle_board()
        print(board)

        return board

    def ai_play(self, board):
        while not ai_game.check_if_the_puzzle_is_solved_except_count_rows(board, 2):
            ai_game.solve_the_puzzle_without_the_last_two_rows(board)
            print(board)
        while not self.check_if_the_puzzle_is_solved(board.board):
            ai_game.solve_the_last_two_rows_fo_the_puzzle(board)

    def user_play(self, board):
        """
        Controls the user moves until the puzzle is solved.
        """
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
