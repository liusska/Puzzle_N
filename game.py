from boards import Board


class Game:

    @staticmethod
    def check_is_the_puzzle_solved(board):
        """
        Check cell by cell if the current puzzle state is equal to solved puzzle state.
        If is equal returns True, else False.
        """
        solved_board_init = Board(len(board))
        solved_board_state = solved_board_init.board
        current_board_state = board
        for row in range(len(solved_board_state)):
            for col in range(len(solved_board_state)):
                if not current_board_state[row][col] == solved_board_state[row][col]:
                    return False
        return True
