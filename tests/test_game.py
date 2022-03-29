import unittest
from puzzleN.boards import Board
from puzzleN.game import Game


class BoardTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.board = Board(4)
        self.board.create_board_for_test(self.game.BOARD_FOR_TEST)

    def test_if_the_solved_puzzle_state_is_actually_solved(self):
        self.board.move_down()
        self.board.move_right()
        self.board.move_right()

        self.assertEqual(self.board.winning_board, self.board.board)

    def test_if_the_puzzle_is_solved_returns_true(self):
        self.board.move_down()
        self.board.move_right()
        self.board.move_right()

        result = self.game.check_if_the_puzzle_is_solved(self.board.board)
        self.assertEqual(True, result)

    def test_if_the_puzzle_is_not_solved_returns_false(self):
        result = self.game.check_if_the_puzzle_is_solved(self.board.board)
        self.assertEqual(False, result)

    def test_control_the_actions_make_correct_up_move(self):
        self.game.control_the_actions(self.board, 'w')
        self.assertEqual(self.board.EMPTY_CELL, self.board.board[1][1])
        self.board.board[1][1] = 6
        self.board.board[2][1] = self.board.EMPTY_CELL

    def test_control_the_actions_make_correct_down_move(self):
        self.game.control_the_actions(self.board, 's')
        self.assertEqual(self.board.EMPTY_CELL, self.board.board[3][1])
        self.board.board[3][1] = 10
        self.board.board[2][1] = self.board.EMPTY_CELL

    def test_control_the_actions_make_correct_left_move(self):
        self.game.control_the_actions(self.board, 'a')
        self.assertEqual(self.board.EMPTY_CELL, self.board.board[2][0])
        self.board.board[2][0] = 9
        self.board.board[2][1] = self.board.EMPTY_CELL

    def test_control_the_actions_make_correct_right_move(self):
        self.game.control_the_actions(self.board, 'd')
        self.assertEqual(self.board.EMPTY_CELL, self.board.board[2][2])
        self.board.board[2][2] = 11
        self.board.board[2][1] = self.board.EMPTY_CELL

