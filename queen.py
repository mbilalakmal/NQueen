# -----------------------------------------------------------
# This module solves N-Queen problem recursively.
# (1) Create a Board object
# (2) Pass it to place_queen function
# (3) The occupancy_matrix attribute contains the solution
#
#
# (C) 2020 Muhammad Bilal Akmal, 17K-3669
# -----------------------------------------------------------

import itertools

import numpy as np


class Board:
    def __init__(self, size: int=4):
        # represents positions of queens. True means a queen is there.
        self._occupancy_matrix = np.zeros(shape=(size,size), dtype=bool)
        
        # represents safe cells. 0 means no queen is attacking this cell.
        self._attacking_matrix = np.zeros(shape=(size,size), dtype=int)
        
        self._size = size

    def describe(self):
        '''
        Describe the positions of queens.
        '''
        print(np.argwhere(self._occupancy_matrix==True))


def place_queen(board: Board, row: int=0):
    '''
    Recursive function that places a queen at `row`.

    Returns `False` if a solution can not be found.
    '''
    # base case
    if row == board._size:
        return True

    # attempt to place a queen in any cell in this row
    for column in range(board._size):
        if not _can_place(board, row, column):
            continue

        # update the board
        _update_board(board, row, column)

        # recursive call for next queen
        if place_queen(board, row+1) == True:
            return True # solution is found

        # remove the queen from the board
        _update_board(board, row, column, False)

    return False


def _can_place(board: Board, row: int, column: int):
    '''
    Return `True` if a queen can be placed at [`row`][`column`].
    '''
    return board._attacking_matrix[row][column] == 0


def _update_board(board: Board, row: int, column: int, forward: bool=True):
    '''
    Update the [`row`][`column`] cell.

    If `forward` is false, the queen at [`row`][`column`] is removed.
    '''
    # update the occupancy_matrix
    board._occupancy_matrix[row][column] = forward

    # update the attacking_matrix
    for coordinate in itertools.product(range(board._size), repeat=2):
        x, y = coordinate
        if(
            x == row or
            y == column or
            (x-y) == (row-column) or
            (x+y) == (row+column)
        ):
            board._attacking_matrix[x][y] += 1 if forward else -1


if __name__ == '__main__':
    size = input('Enter size of the board: ')
    board = Board(int(size))
    place_queen(board)
    board.describe()