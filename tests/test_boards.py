import unittest
from boards import Board


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = Board(4)

    def test_is_the_board_attributes_set_correctly(self):
        self.assertEqual(4, self.game_board.side)
        self.assertEqual(16, self.game_board.fields_count)
        self.assertEqual(list, type(self.game_board.initialize_sorted_board()))
        self.assertEqual(4, len(self.game_board.possible_moves))

    def test_is_the_board_initialized_correctly(self):
        expected = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ' ']]
        actual = self.game_board.board
        self.assertEqual(expected, actual)

    def test_shuffle_board(self):
        array_initialize = self.game_board.board
        array_after_shuffle = self.game_board.shuffle_board()
        self.assertNotEqual(array_initialize, array_after_shuffle)

    def test_is_finding_target_cell_correctly(self):
        actual_coordinates = (
            len(self.game_board.initialize_sorted_board()) - 1,
            len(self.game_board.initialize_sorted_board()) - 1
        )
        expected_coordinates = self.game_board.find_target_cell()
        self.assertEqual(actual_coordinates, expected_coordinates)

    def test_is_valid_move_with_correct_coordinates_returns_true(self):
        self.assertEqual(True, self.game_board.is_valid_move(0, 0))
        self.assertEqual(True, self.game_board.is_valid_move(1, 2))
        self.assertEqual(True, self.game_board.is_valid_move(3, 3))

    def test_is_valid_move_with_incorrect_coordinates_returns_false(self):
        self.assertEqual(False, self.game_board.is_valid_move(1, -4))
        self.assertEqual(False, self.game_board.is_valid_move(4, 4))
        self.assertEqual(False, self.game_board.is_valid_move(1, 4))

    def test_move_left_empty_cell_correctly(self):
        row, col = self.game_board.find_target_cell()
        self.game_board.move_left()
        new_row, new_col = self.game_board.find_target_cell()
        self.assertEqual((row, col-1), (new_row, new_col))

    def test_move_right_empty_cell_correctly(self):
        row, col = self.game_board.find_target_cell()
        self.game_board.move_left()
        self.game_board.move_left()
        self.game_board.move_left()
        self.game_board.move_up()
        self.game_board.move_right()
        new_row, new_col = self.game_board.find_target_cell()
        self.assertEqual((row-1, col-2), (new_row, new_col))

    def test_move_up_empty_cell_correctly(self):
        row, col = self.game_board.find_target_cell()
        self.game_board.move_up()
        new_row, new_col = self.game_board.find_target_cell()
        self.assertEqual((row-1, col), (new_row, new_col))

    def test_move_down_empty_cell_correctly(self):
        row, col = self.game_board.find_target_cell()
        self.game_board.move_up()
        self.game_board.move_up()
        self.game_board.move_up()
        self.game_board.move_left()
        self.game_board.move_down()

        new_row, new_col = self.game_board.find_target_cell()
        self.assertEqual((row - 2, col - 1), (new_row, new_col))

    def test_make_move_returns_correct_element(self):
        self.assertEqual(int, type(self.game_board.make_move(0, 2)))
        self.assertEqual(int, type(self.game_board.make_move(1, 3)))

    def test_make_move_returns_incorrect_element(self):
        with self.assertRaises(Exception) as ex:
            self.game_board.make_move(4, 4)
        self.assertEqual('list index out of range', str(ex.exception))

    def test_class_str_representation(self):
        expected = '1  2  3  4  \n5  6  7  8  \n9  10 11 12 \n13 14 15    \n'
        actual = self.game_board.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
