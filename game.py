from puzzleN.boards import Board


class Game:
    """
    This class cares about the game.
    """

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
    def solve_the_puzzle(board, game):
        """
        Take the user input (one or more) for up, down, left or right and
        call the control_the_input_actions with the given params
        """
        print('Enter move: ')
        directions = input().split()
        game.control_the_actions(board, directions)
        print(board)

    @staticmethod
    def check_if_the_puzzle_is_solved(board):
        """
        Check cell by cell if the current puzzle state is equal to solved puzzle state.
        If is equal prints a message and returns True, else False.
        """
        solved_board_state = Board(len(board)).board
        current_board_state = board

        for row in range(len(solved_board_state)):
            for col in range(len(solved_board_state)):
                if not current_board_state[row][col] == solved_board_state[row][col]:
                    return False

        print("*** The puzzle is SOLVED! ***")
        return True
