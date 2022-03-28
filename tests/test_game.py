import unittest
from puzzleN.boards import Board
from puzzleN.game import Game


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.board = Board(4)
        self.board.create_board_for_test()

    def test_if_the_solved_puzzle_state_is_actually_solved(self):
        board_solved_state = Board(4)
        self.board.move_down()
        self.board.move_right()
        self.board.move_right()

        self.assertEqual(board_solved_state.board, self.board.board)

    def test_if_the_puzzle_is_solved_returns_true(self):
        self.board.move_down()
        self.board.move_right()
        self.board.move_right()

        result = self.game.check_if_the_puzzle_is_solved(self.board.board)
        self.assertEqual(True, result)

    def test_if_the_puzzle_is_not_solved_returns_false(self):
        self.board.move_up()
        self.board.move_left()
        self.board.move_up()

        result = self.game.check_if_the_puzzle_is_solved(self.board.board)
        self.assertEqual(False, result)
