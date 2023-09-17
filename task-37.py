"""
Sudoku 9x9 solver
"""
from copy import deepcopy

all_boards = []


def get_suit_digits(arr: [int]) -> {int}:
    return set(range(10)).difference(set(arr))


def transform_board(arr: [[str]]) -> [[int]]:
    brd = []
    for row in arr:
        brd.append(list(map(lambda x: 0 if x == '.' else int(x), row)))
    return brd


class Board:
    def __init__(self, board: [[int]]):
        self.board = board

    def row(self, i) -> [int]:
        return self.board[i]

    def col(self, i) -> [int]:
        return [self.board[_][i] for _ in range(9)]

    def sub_box(self, row: int, col: int) -> [int]:
        r = []
        a, b = row - row % 3, col - col % 3
        for i in range(a, a + 3):
            for j in range(b, b + 3):
                r.append(self.board[i][j])
        return r

    def get_null_cells(self) -> [(int, int)]:
        r = []
        for i, row in enumerate(self.board):
            for j, digit in enumerate(row):
                if digit == 0:
                    r.append((i, j))
        return r

    def get_suit_digits_set(self, i, j) -> {int}:
        a = get_suit_digits(self.row(i))
        b = get_suit_digits(self.col(j))
        c = get_suit_digits(self.sub_box(i, j))
        return a.intersection(b).intersection(c)

    def process_board(self) -> (int, int):
        while 1:
            m, u, v = 10, -1, -1
            ns = self.get_null_cells()
            if len(ns) == 0:
                return 10, 10
            for i, j in ns:
                sx = self.get_suit_digits_set(i, j)
                x = len(sx)
                if x == 0:
                    return -1, -1
                if x == 1:
                    self.board[i][j] = sx.pop()
                if x < m:
                    m, u, v = x, i, j
            if m > 1:
                break
        return u, v


def solveSudoku(board: [[str]]) -> None:
    global all_boards

    all_boards = [Board(transform_board(board))]

    while 1:
        new_all_boards = []
        for b in all_boards:
            u, v = b.process_board()
            if (u, v) == (10, 10):
                for i, row in enumerate(b.board):
                    for j, s in enumerate(row):
                        board[i][j] = str(s)
                for r in board:
                    print(r)
                return
            if (u, v) == (-1, -1):
                continue
            for d in b.get_suit_digits_set(u, v):
                new_board = deepcopy(b.board)
                new_board[u][v] = d
                new_all_boards.append(Board(new_board))
        all_boards = new_all_boards


solveSudoku(
    [["9", ".", ".", "7", "6", "8", ".", ".", "3"],
     [".", ".", ".", ".", ".", "5", "9", ".", "."],
     [".", ".", "5", ".", ".", ".", ".", "6", "8"],
     # ---------------------------------------------
     [".", ".", "9", "8", ".", "2", ".", ".", "5"],
     ["7", ".", ".", ".", "9", ".", "8", ".", "."],
     [".", ".", ".", ".", "3", ".", ".", ".", "."],
     # ---------------------------------------------
     [".", "2", ".", ".", ".", ".", ".", "7", "4"],
     [".", ".", ".", "1", ".", ".", ".", ".", "."],
     [".", "7", ".", ".", ".", "4", "1", ".", "."]]
)

'''
from copy import deepcopy

all_boards = []

def get_suit_digits(arr: [int]) -> {int}:
    return set(range(10)).difference(set(arr))

def transform_board(arr: [[str]]) -> [[int]]:
    brd = []
    for row in arr:
        brd.append(list(map(lambda x: 0 if x == '.' else int(x), row)))
    return brd


class Board:
    def __init__(self, board: [[int]]):
        self.board = board

    def print_board(self) -> None:
        for row in self.board:
            print(row)
        print()

    def row(self, i) -> [int]:
        return self.board[i]

    def col(self, i) -> [int]:
        return [self.board[_][i] for _ in range(9)]

    def sub_box(self, row: int, col: int) -> [int]:
        r = []
        a, b = row - row % 3, col - col % 3
        for i in range(a, a + 3):
            for j in range(b, b + 3):
                r.append(self.board[i][j])
        return r

    def get_null_cells(self) -> [(int, int)]:
        r = []
        for i, row in enumerate(self.board):
            for j, digit in enumerate(row):
                if digit == 0:
                    r.append((i, j))
        return r

    def get_suit_digits_set(self, i, j) -> {int}:
        a = get_suit_digits(self.row(i))
        b = get_suit_digits(self.col(j))
        c = get_suit_digits(self.sub_box(i, j))
        return a.intersection(b).intersection(c)

    def process_board(self) -> (int, int):
        while 1:
            m, u, v = 10, -1, -1
            ns = self.get_null_cells()
            if len(ns) == 0:
                return 10, 10
            for i, j in ns:
                sx = self.get_suit_digits_set(i, j)
                x = len(sx)
                if x == 0:
                    return -1, -1
                if x == 1:
                    self.board[i][j] = sx.pop()
                if x < m:
                    m, u, v = x, i, j
            if m > 1:
                break
        return u, v


def solveSudoku() -> None:

    global all_boards

    brd = Board(transform_board(
        [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]
    ))
    all_boards.append(brd)
    while 1:
        new_all_boards = []
        for b in all_boards:
            u, v = b.process_board()
            if (u, v) == (10, 10):
                b.print_board()
                return
            if (u, v) == (-1, -1):
                continue
            for d in b.get_suit_digits_set(u, v):
                new_board = deepcopy(b.board)
                new_board[u][v] = d
                new_all_boards.append(Board(new_board))
        all_boards = new_all_boards


solveSudoku()
'''
