class Matrix:
    def __init__(self, size: int):
        if size < 2:
            self.matrix = []
        k = 1
        self.matrix = []
        self.size = size
        for i in range(size):
            r = []
            for j in range(size):
                r.append(k)
                k += 1
            self.matrix.append(r)

    def prn(self):
        for i in range(self.size):
            s = ''
            for j in range(self.size):
                x = str(self.matrix[i][j])
                s += ' ' * (self.size - len(x)) + x + ' '
            print(s)
        print()

    def trans_pos(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

    def column_swap(self, x, y):
        for i in range(self.size):
            self.matrix[i][x], self.matrix[i][y] = self.matrix[i][y], self.matrix[i][x]

    def clockwise_rotate(self):
        self.trans_pos()
        for i in range(self.size >> 1):
            self.column_swap(i, self.size - i - 1)


def rotate(matrix: [[int]]) -> None:
    # transposition
    size = len(matrix)
    if size < 2:
        return matrix
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # column swapping
    for i in range(size >> 1):
        for j in range(size):
            matrix[j][i], matrix[j][size - i - 1] = matrix[j][size - i - 1], matrix[j][i]
    return matrix

assert (rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
assert (rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) ==
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])


x = Matrix(10)
x.clockwise_rotate()
x.prn()
