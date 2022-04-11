def find_next_unordered_value(current_board, ordered_board):
    for r in range(len(current_board)):
        for c in range(len(current_board)):
            if current_board[r][c] != ordered_board[r][c]:
                return ordered_board[r][c]
    return False


def ai_moves_control(board, value_to_order, value_cell_coordinates, empty_cell_coordinates, correct_cell_coordinates):
    correct_row, correct_col = correct_cell_coordinates
    value_row, value_col = value_cell_coordinates

    # Last two rows moves
    if correct_row in range(board.side - 2, board.side):
        print("Last 2 rows moves")
        exit()

    # Last two columns moves
    elif correct_col in range(board.side - 2, board.side):
        make_last_two_columns_moves(
            board,
            value_to_order,
            correct_cell_coordinates
        )

    value_cell_coordinates = board.find_target_cell(value_to_order, board.board)
    while value_cell_coordinates != correct_cell_coordinates:
        # If element is in the last column in unordered board
        empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
        if value_col == board.side - 1:
            move_element_from_last_column(
                board,
                value_cell_coordinates,
                empty_cell_coordinates
            )

        # If the element is in the first unordered row
        value_cell_coordinates = board.find_target_cell(value_to_order, board.board)
        value_row, value_col = value_cell_coordinates
        empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
        if value_row == correct_row:
            move_element_on_same_row(
                board,
                value_to_order,
                value_cell_coordinates,
                empty_cell_coordinates,
                correct_cell_coordinates
            )

        value_cell_coordinates = board.find_target_cell(value_to_order, board.board)
        while value_cell_coordinates != correct_cell_coordinates:
            empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
            standard_cells_moves_when_the_correct_cell_is_not_down_or_in_the_end(
                board,
                value_to_order,
                value_cell_coordinates,
                empty_cell_coordinates,
                correct_cell_coordinates
            )
            value_cell_coordinates = board.find_target_cell(value_to_order, board.board)

        break
    return


def set_last_column_specific_case(board):
    board.move_down()
    board.move_right()
    board.move_up()
    board.move_left()
    board.move_up()
    board.move_right()
    board.move_down()
    board.move_down()
    board.move_left()
    board.move_up()
    board.move_right()
    board.move_up()
    board.move_left()
    board.move_down()
    board.move_down()
    board.move_right()
    board.move_up()
    board.move_up()
    board.move_left()
    board.move_down()


def set_last_two_columns_elements(board):
    board.move_up()
    board.move_left()
    board.move_down()


def swap_cells_to_right_from_down_with_moves_from_left_down_right_up_left(board):
    board.move_down()
    board.move_right()
    board.move_right()
    board.move_up()
    board.move_left()


def swap_cells_to_left_from_down_with_moves_from_right_down_left_up_right(board):
    board.move_down()
    board.move_left()
    board.move_left()
    board.move_up()
    board.move_right()


def swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board):
    board.move_up()
    board.move_left()
    board.move_down()


def swap_cells_to_right_from_down_with_moves_from_right_left_down_right_up(board):
    board.move_left()
    board.move_down()
    board.move_right()
    board.move_right()
    board.move_up()


def move_element_from_last_column(board, value_cell, empty_cell):
    value_row, value_col = value_cell
    empty_row, empty_col = empty_cell

    if empty_row == value_row:
        while not empty_col == value_col:
            board.move_right()
            empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            # '1' '0'

    elif empty_row < value_row:
        if empty_col == value_col:
            while not empty_row == value_row:
                board.move_down()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)

            board.move_left()
            board.move_up()
            board.move_right()
            # '1' '0'

        elif empty_col < value_col:
            while not empty_row == value_row:
                board.move_down()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)

            while not empty_col == value_col:
                board.move_right()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            # '1' '0'

    elif empty_row > value_row:
        if empty_col < value_col:
            while not empty_col == value_col:
                board.move_right()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)

            while not empty_row == value_row + 1:
                board.move_up()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)

            board.move_left()
            board.move_up()
            board.move_right()
            # '1' '0'

        elif empty_col == value_col:
            while not empty_row == value_row + 1:
                board.move_up()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)

            board.move_right()
            board.move_up()
            board.move_right()
            # '1' '0'


def set_the_empty_cell_right_to_the_target_value(board, value_cell, empty_cell):
    value_row, value_col = value_cell
    empty_row, empty_col = empty_cell

    if empty_row == value_row:
        if empty_col > value_col:
            while not empty_col == value_col + 1:
                board.move_left()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            # '1' '0'

        elif empty_col < value_col:
            while not empty_col == value_col:
                board.move_right()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            # '1' '0'

    elif empty_row > value_row:
        if empty_col > value_col:
            while not empty_row == value_row:
                board.move_up()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            while not empty_col == value_col + 1:
                board.move_left()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            # '1' '0'

        elif empty_col < value_col:
            while not empty_col == value_col - 1:
                board.move_right()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            while not empty_row == value_row:
                board.move_up()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            board.move_right()
            # '1' '0'

        elif empty_col == value_col:
            while not empty_row == value_row + 1:
                board.move_up()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            board.move_right()
            board.move_up()
            # '1' '0'

    elif empty_row < value_row:
        if empty_col == value_col:
            if empty_col < board.side - 1:
                board.move_right()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
                while not empty_row == value_row:
                    board.move_down()
                    empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            else:
                while not empty_row == value_row - 1:
                    board.move_down()
                    empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
                board.move_left()
                board.move_down()
                board.move_right()
            # '1' '0'

        elif empty_col < value_col:
            while not empty_col == value_col:
                board.move_right()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            while not empty_row == value_row - 1:
                board.move_down()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            board.move_left()
            board.move_down()
            board.move_right()
            # '1' '0'

        elif empty_col > value_col:
            while not empty_row == value_row:
                board.move_down()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            while not empty_col == value_col + 1:
                board.move_left()
                empty_row, empty_col = board.find_target_cell(board.EMPTY_CELL, board.board)
            # '1' '0'


def move_element_on_same_row(board, target_value, value_cell, empty_cell, correct_cell):
    set_the_empty_cell_right_to_the_target_value(board, value_cell, empty_cell)
    value_cell = board.find_target_cell(target_value, board.board)
    while not value_cell == correct_cell:
        if value_cell[1] < correct_cell[1]:
            swap_cells_to_right_from_down_with_moves_from_right_left_down_right_up(board)

        else:
            swap_cells_to_left_from_down_with_moves_from_right_down_left_up_right(board)

        value_cell = board.find_target_cell(target_value, board.board)
        empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
        set_the_empty_cell_right_to_the_target_value(board, value_cell, empty_cell)


def standard_cells_moves_when_the_correct_cell_is_not_down_or_in_the_end(
        board,
        value,
        value_cell_coordinates,
        empty_cell_coordinates,
        correct_cell_coordinates):

    correct_row, correct_col = correct_cell_coordinates
    value_row, value_col = value_cell_coordinates
    set_the_empty_cell_right_to_the_target_value(board, value_cell_coordinates, empty_cell_coordinates)

    if value_row > correct_row:
        if value_col == correct_col:
            while not value_row == correct_row:
                swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board)
                value_row, value_col = board.find_target_cell(value, board.board)

                if value_row != correct_row:
                    board.move_right()
                    board.move_up()

        elif value_col < correct_col:
            while not value_row == correct_row + 1:
                swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board)
                value_row, value_col = board.find_target_cell(value, board.board)

                if value_row != correct_row:
                    board.move_right()
                    board.move_up()
            while not value_col == correct_col:
                board.move_left()
                swap_cells_to_right_from_down_with_moves_from_left_down_right_up_left(board)
                value_cell_coordinates = board.find_target_cell(value, board.board)

                value_row, value_col = value_cell_coordinates

        elif value_col > correct_col:
            while not value_row == correct_row:
                value_cell_coordinates = board.find_target_cell(value, board.board)
                empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
                set_the_empty_cell_right_to_the_target_value(board, value_cell_coordinates, empty_cell_coordinates)
                swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board)

                value_cell_coordinates = board.find_target_cell(value, board.board)
                value_row, value_col = value_cell_coordinates
                if not value_row == correct_row:
                    board.move_right()
                    board.move_up()

            while not value_col == correct_col:
                empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
                set_the_empty_cell_right_to_the_target_value(board, value_cell_coordinates, empty_cell_coordinates)
                swap_cells_to_left_from_down_with_moves_from_right_down_left_up_right(board)
                value_cell_coordinates = board.find_target_cell(value, board.board)
                value_row, value_col = value_cell_coordinates

    value_cell_coordinates = board.find_target_cell(value, board.board)
    empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
    set_the_empty_cell_right_to_the_target_value(board, value_cell_coordinates, empty_cell_coordinates)

    value_row, value_col = value_cell_coordinates
    if value_row == correct_row:
        if value_cell_coordinates != correct_cell_coordinates:
            move_element_on_same_row(board, value, value_cell_coordinates, empty_cell_coordinates, correct_cell_coordinates)


def make_last_two_columns_moves(board, target_value, correct_cell):
    last_columns_move_for_next_value(board, target_value, correct_cell)

    last_columns_move_for_current_value(board, target_value, correct_cell)


def last_columns_move_for_next_value(board, target_value, correct_cell):
    next_value = target_value + 1
    next_value_coordinates = board.find_target_cell(next_value, board.board)
    correct_row, correct_col = correct_cell
    empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
    set_the_empty_cell_right_to_the_target_value(board, next_value_coordinates, empty_cell)

    if correct_col == board.side - 1:
        move_element_from_last_column(board, next_value_coordinates, empty_cell)
    next_value_coordinates = board.find_target_cell(next_value, board.board)

    while next_value_coordinates != correct_cell:
        next_value_row, next_value_col = next_value_coordinates
        empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)

        if next_value_row == correct_row:
            move_element_on_same_row(board, next_value, next_value_coordinates, empty_cell, correct_cell)

        else:
            standard_cells_moves_when_the_correct_cell_is_not_down_or_in_the_end(
                board,
                next_value,
                next_value_coordinates,
                empty_cell,
                correct_cell
            )

        next_value_coordinates = board.find_target_cell(next_value, board.board)
    print(board)


def last_columns_move_for_current_value(board, target_value, correct_cell):
    target_value_coordinates = board.find_target_cell(target_value, board.board)
    current_target_row, current_target_col = target_value_coordinates

    correct_cell = ((correct_cell[0] + 1), correct_cell[1])
    correct_row, correct_col = correct_cell
    empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
    set_the_empty_cell_right_to_the_target_value(board, target_value_coordinates, empty_cell)

    if current_target_col == board.side - 1:
        target_value_coordinates = board.find_target_cell(target_value, board.board)
        move_element_from_last_column(board, target_value_coordinates, empty_cell)

    empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
    target_value_coordinates = board.find_target_cell(target_value, board.board)
    set_the_empty_cell_right_to_the_target_value(board, target_value_coordinates, empty_cell)

    target_value_coordinates = board.find_target_cell(target_value, board.board)
    current_target_row, current_target_col = target_value_coordinates

    while target_value_coordinates != correct_cell:
        if current_target_row == correct_row:
            move_element_on_same_row(board, target_value, target_value_coordinates, empty_cell, correct_cell)
        else:
            standard_cells_moves_when_the_correct_cell_is_not_down_or_in_the_end(board, target_value,
                                                                                 target_value_coordinates,
                                                                                 empty_cell,
                                                                                 correct_cell)
        empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
        target_value_coordinates = board.find_target_cell(target_value, board.board)
        current_target_row, current_target_col = target_value_coordinates

    set_the_empty_cell_right_to_the_target_value(board, target_value_coordinates, empty_cell)
    set_last_two_columns_elements(board)

    if board.board[correct_row - 1][correct_col + 1] != board.winning_board[correct_row - 1][correct_col + 1]:
        set_last_column_specific_case(board)





