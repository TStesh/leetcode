"""
Determine if a 9 x 9 Sudoku board is valid.

Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


def check(arr: [int]) -> bool:
    d = {}
    for digit in arr:
        if digit > 0 and digit in d:
            return False
        else:
            d[digit] = 1
    return True


class Board:
    def __init__(self, board: [[str]]):
        self.board = []
        self.size = len(board)
        for row in board:
            self.board.append(
                list(map(lambda x: 0 if x == '.' else int(x), row))
            )

    def check_rows(self) -> bool:
        for row in self.board:
            if not check(row):
                return False
        return True

    def check_columns(self) -> bool:
        for i in range(self.size):
            col = [self.board[_][i] for _ in range(self.size)]
            if not check(col):
                return False
        return True

    def get_sub_box(self, row: int, col: int) -> [int]:
        r = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                r.append(self.board[i][j])
        return r

    def check_sub_boxes(self) -> bool:
        for i in range(0, self.size, 3):
            for j in range(0, self.size, 3):
                if not check(self.get_sub_box(i, j)):
                    return False
        return True

    def output(self) -> [[str]]:
        r = []
        for row in self.board:
            r.append(list(map(str, row)))
        return r


x = Board(
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
)

print(x.check_rows() and x.check_columns() and x.check_sub_boxes())


