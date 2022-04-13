def find_next_unordered_value(current_board, ordered_board):
    """
    Compare the elements of the current board with the elements from the ordered board by indexes.
    Returns the first unordered value if there is else returns False.

    """
    for r in range(len(current_board)):
        for c in range(len(current_board)):
            if current_board[r][c] != ordered_board[r][c]:
                return ordered_board[r][c]
    return False


def check_if_the_puzzle_is_solved_except_count_rows(board, minus_rows):
    """
    If the AI is on his first step for solving the puzzle we have to check the board without the last 2 rows.
        minus-rows will be equal to 2.
    If the AI is on his second and last step, the minus-rows will be equal to zero,
     and the function will check all rows.
    """
    for row in range(board.side - minus_rows):
        for col in range(board.side):
            if board.board[row][col] != board.winning_board[row][col]:
                return False
    return True


def solve_the_puzzle_without_the_last_two_rows(board):
    """
    Calls the function that controls the moves of the AI, depending on the coordinates of the
    current unordered value, the coordinates of this value and the correct cell coordinates if
    they are not in the last two rows.
    """
    current_unordered_value = find_next_unordered_value(board.board, board.winning_board)
    value_cell_coordinates = board.find_target_cell(current_unordered_value, board.board)
    correct_cell_coordinates = board.find_target_cell(current_unordered_value, board.winning_board)

    ai_moves_control(
        board,
        current_unordered_value,
        value_cell_coordinates,
        correct_cell_coordinates
    )
    value_cell_coordinates = board.find_target_cell(current_unordered_value, board.board)
    if value_cell_coordinates == correct_cell_coordinates:
        return True
    return False


def ai_moves_control(board, value_to_order, value_cell_coordinates, correct_cell_coordinates):
    """
    This is the main function that controls the steps for solving the puzzle from first to n-2 row.
     First we checked if the correct coordinates are for the last two columns order.
     If they are, after the move the function ends.
     Else we make moves till the target value is in the correct position.
        If the correct cell is in the other part of the puzzle, before the order we have to check
        if the value is in the last column and move it from there.
        Then we have to check if the target is or not on the correct row and call the correct
        for the needed move function.
    """
    correct_row, correct_col = correct_cell_coordinates
    value_row, value_col = value_cell_coordinates

    # If the correct cell is in last two columns.
    if correct_col in range(board.side - 2, board.side):
        make_last_two_columns_moves(
            board,
            value_to_order,
            correct_cell_coordinates
        )
        return

    # If element is in the last column in unordered board
    empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
    if value_col == board.side - 1:
        move_element_from_last_column(
            board,
            value_cell_coordinates,
            empty_cell_coordinates
        )

        value_cell_coordinates = board.find_target_cell(value_to_order, board.board)
        value_row, value_col = value_cell_coordinates

    # If the element is in the first unordered row
    if value_row == correct_row:
        move_element_on_same_row(
            board,
            value_to_order,
            value_cell_coordinates,
            correct_cell_coordinates
        )

    else:
        empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
        standard_cells_moves_with_no_special_cases(
            board,
            value_to_order,
            value_cell_coordinates,
            empty_cell_coordinates,
            correct_cell_coordinates
        )


def update_the_position_of_the_empty_cell_next_to_the_value(board, value):
    """
    Check where are the value coordinates, the empty cell coordinates and call the function
     that set the empty field next to the value cell.
    """
    value_cell_coordinates = board.find_target_cell(value, board.board)
    empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
    set_the_empty_cell_right_to_the_target_value(board, value_cell_coordinates, empty_cell_coordinates)


def set_last_column_specific_case(board):
    """
        Used for a special for the last two column case:
        When the two cell that have to be order in a column before been slapped on the correct cells
        are positioned on a diagonal next to each other with the empty cell up between then.
    """
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
    """
    When the last two elements of the row are positioned in a column,
     after this moves they will be on the correct for the row places.
    """
    board.move_up()
    board.move_left()
    board.move_down()


def swap_cells_to_right_from_down_with_moves_from_left_down_right_up_left(board):
    """
    Swap the value cell to right from bottom side with specific for the position moves.
    """
    board.move_down()
    board.move_right()
    board.move_right()
    board.move_up()


def swap_cells_to_left_from_down_with_moves_from_right_down_left_up_right(board):
    """
    Swap the value cell to left from bottom side with specific for the position moves.
    """
    board.move_down()
    board.move_left()
    board.move_left()
    board.move_up()
    board.move_right()


def swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board):
    """
    Swap the value cell to right from upper side with specific for the position moves.
    """
    board.move_up()
    board.move_left()
    board.move_down()


def swap_cells_to_right_from_down_with_moves_from_right_left_down_right_up(board):
    """
    Swap the value cell to right from bottom side with specific for the position moves.
    """
    board.move_left()
    board.move_down()
    board.move_right()
    board.move_right()
    board.move_up()


def move_element_from_last_row(board):
    """
    After the empty cell is set next to the target value, with the next steps the value
     will be not on the last row anymore and the empty cell is set again next to the value.
    """
    board.move_up()
    board.move_left()
    board.move_down()
    board.move_right()
    board.move_up()


def move_element_from_last_column(board, value_cell, empty_cell):
    """
    After the value row is checked this function makes moves till the empty cell is not next to the target value,
     and if there is need makes extra moves while the empty cell is positioned to the right of the target value.
    """
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
    """
    According to the target value coordinates and the empty cell coordinates, this
     function moves the empty cell in right of the target value.
    """
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


def move_element_on_same_row(board, target_value, value_cell, correct_cell):
    """
    According to the position (column) of the target value cell to the correct value cell,
     when they are positioned on one row.
     We have two cases depends on that if the move is for the last two columns order on row-1
     or is for order
    """
    empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
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


def standard_cells_moves_with_no_special_cases(
        board,
        value,
        value_cell_coordinates,
        empty_cell_coordinates,
        correct_cell_coordinates):

    """
    In this case we accept that the value row is always more than the correct row.
    According to the value column and the correct column, this function makes moves in up, right or left.
    """
    correct_row, correct_col = correct_cell_coordinates
    value_row, value_col = value_cell_coordinates
    set_the_empty_cell_right_to_the_target_value(board, value_cell_coordinates, empty_cell_coordinates)

    if value_col == correct_col:
        while not value_row == correct_row:
            swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board)
            value_row, value_col = board.find_target_cell(value, board.board)

            if value_row != correct_row:
                board.move_right()
                board.move_up()

    elif value_col < correct_col:
        if value_row == board.side - 1:
            move_element_from_last_row(board)
            value_row, value_col = board.find_target_cell(value, board.board)
        if value_row > correct_row + 1:
            while not value_row == correct_row + 1:
                swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board)
                value_row, value_col = board.find_target_cell(value, board.board)
                if value_row != correct_row:
                    board.move_right()
                    board.move_up()
                    value_row, value_col = board.find_target_cell(value, board.board)
        while not value_col == correct_col:
            board.move_left()
            swap_cells_to_right_from_down_with_moves_from_left_down_right_up_left(board)
            value_row, value_col = board.find_target_cell(value, board.board)

    elif value_col > correct_col:
        while not value_row == correct_row:
            update_the_position_of_the_empty_cell_next_to_the_value(board, value)
            swap_cells_to_up_from_right_with_moves_from_right_up_left_down(board)

            value_cell_coordinates = board.find_target_cell(value, board.board)
            value_row, value_col = value_cell_coordinates
            if not value_row == correct_row:
                board.move_right()
                board.move_up()

        while not value_col == correct_col:
            update_the_position_of_the_empty_cell_next_to_the_value(board, value)
            swap_cells_to_left_from_down_with_moves_from_right_down_left_up_right(board)
            value_cell_coordinates = board.find_target_cell(value, board.board)
            value_row, value_col = value_cell_coordinates

    update_the_position_of_the_empty_cell_next_to_the_value(board, value)


def make_last_two_columns_moves(board, target_value, correct_cell):
    """
    With the first function call we set the last correct value for the row in position [row][column-1]
    With the second function call we set the last-1 correct value for the row in position [row + 1][column-1]
    Then trey are prepared for the special order for the last two columns.
    """
    last_columns_move_for_next_value(board, target_value, correct_cell)

    last_columns_move_for_current_value(board, target_value, correct_cell)


def last_columns_move_for_next_value(board, target_value, correct_cell):
    """
    After increasing the target value with 1, we know what is the next value
     for order, before the current.
     Before the moves for order we have to check if the value is in the last column
     and move out it from there.
     After that we can start moving the value according the coordinates of the value
      and the correct position.
    """
    next_value = target_value + 1
    next_value_coordinates = board.find_target_cell(next_value, board.board)
    correct_row, correct_col = correct_cell
    empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)

    if next_value_coordinates[1] == board.side - 1:
        move_element_from_last_column(board, next_value_coordinates, empty_cell)
    next_value_coordinates = board.find_target_cell(next_value, board.board)

    set_the_empty_cell_right_to_the_target_value(board, next_value_coordinates, empty_cell)

    while next_value_coordinates != correct_cell:
        next_value_row, next_value_col = next_value_coordinates
        empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)

        if next_value_row == correct_row:
            move_element_on_same_row(board, next_value, next_value_coordinates, correct_cell)

        else:
            standard_cells_moves_with_no_special_cases(
                board,
                next_value,
                next_value_coordinates,
                empty_cell,
                correct_cell
            )

        next_value_coordinates = board.find_target_cell(next_value, board.board)
    print(board)


def last_columns_move_for_current_value(board, target_value, correct_cell):
    """
     Before the moves for order the value on a correct cell we have to check if the value is in the last column
     and move out it from there.
     After that we can start moving the value according the coordinates of the value
     and the correct position coordinates.

     In the end we have to check if there is a specific case when the last two values on the row are not set
     correct after the function order.
     This happens when they are positioned on a diagonal next to each other with the empty cell up between then.
    """
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
    update_the_position_of_the_empty_cell_next_to_the_value(board, target_value)

    target_value_coordinates = board.find_target_cell(target_value, board.board)
    current_target_row, current_target_col = target_value_coordinates

    while target_value_coordinates != correct_cell:
        if current_target_row == correct_row:
            move_element_on_same_row(board, target_value, target_value_coordinates, correct_cell)
        else:
            standard_cells_moves_with_no_special_cases(board, target_value,
                                                       target_value_coordinates,
                                                       empty_cell,
                                                       correct_cell)
        empty_cell = board.find_target_cell(board.EMPTY_CELL, board.board)
        target_value_coordinates = board.find_target_cell(target_value, board.board)
        current_target_row, current_target_col = target_value_coordinates

    set_the_empty_cell_right_to_the_target_value(board, target_value_coordinates, empty_cell)
    set_last_two_columns_elements(board)

    if (board.board[correct_row - 1][correct_col] != board.winning_board[correct_row - 1][correct_col]
            or board.board[correct_row - 1][correct_col + 1] != board.winning_board[correct_row - 1][correct_col + 1]):
        set_last_column_specific_case(board)


def last_moves_for_full_solve_puzzle_state(board):
    """
    When the puzzle is almost solve, this steps order last 3 unordered elements
    in range row-2 and column-2
    """
    board.move_right()
    board.move_down()


def swap_last_two_rows_elements_to_correct_places_diff_rows_same_columns(board):
    """
    Whe the first elements from the last two rows are ordered next to each other,
    this steps moves them to their correct places in the beginning of each row or
    just after the last ordered elements.
    """
    board.move_down()
    board.move_left()
    board.move_left()
    board.move_up()
    board.move_right()


def last_two_rows_specific_case(board):
    """
    When the first elements of the last two rows are in the correct column but in reversed order,
    these moves are arranging them next to each other in correct order ready for moving on the
     beginning of the two rows or just after the last ordered elements.
    """
    board.move_down()
    board.move_left()
    board.move_up()
    board.move_right()
    board.move_right()
    board.move_down()

    board.move_left()
    board.move_up()
    board.move_left()
    board.move_down()
    board.move_right()
    board.move_right()
    board.move_up()
    board.move_left()
    board.move_down()
    board.move_right()
    board.move_up()


def solve_the_last_two_rows_for_the_puzzle(board):
    """
    Controls the ordering of the elements two by two until they are in
     correct positions in the 2 rows, same column.
    The last steps is to move the last 3 cells
    """
    row = board.side - 2

    for r in range(row, board.side-1):
        for c in range(0, board.side-2):
            value_on_first_row = board.winning_board[r][c]
            value_on_second_row = board.winning_board[r + 1][c]

            make_last_two_rows_moves(board, value_on_second_row, (r, c))
            if board.board[r + 1][c] == value_on_first_row:
                last_two_rows_specific_case(board)
            else:
                make_last_two_rows_moves(board, value_on_first_row, (r, c + 1))
            swap_last_two_rows_elements_to_correct_places_diff_rows_same_columns(board)

    print(board)
    last_moves_for_full_solve_puzzle_state(board)
    print(board)


def make_last_two_rows_moves(board, value_to_order, correct_cell_coordinates):
    """
    Controls the last two rows moves.
    According to the current value coordinates call the correct function.
    """
    value_coordinates = board.find_target_cell(value_to_order, board.board)
    value_row, value_col = value_coordinates
    empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)

    if value_col == board.side - 1:
        move_element_from_last_column(board, value_coordinates, empty_cell_coordinates)
        empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
        value_coordinates = board.find_target_cell(value_to_order, board.board)

    set_the_empty_cell_right_to_the_target_value(board, value_coordinates, empty_cell_coordinates)
    empty_cell_coordinates = board.find_target_cell(board.EMPTY_CELL, board.board)
    value_row, value_col = value_coordinates

    if value_coordinates != correct_cell_coordinates:
        if value_row == board.side - 1:
            standard_cells_moves_with_no_special_cases(
                board,
                value_to_order,
                value_coordinates,
                empty_cell_coordinates,
                correct_cell_coordinates)
        else:
            move_element_on_same_row(
                board,
                value_to_order,
                value_coordinates,
                correct_cell_coordinates
            )





