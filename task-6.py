"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
display this pattern in a fixed font for better legibility) P   A   H   N A P L S I I G Y   I   R And then read line
by line: "PAHNAPLSIIGYIR". Write the code that will take a string and make this conversion given a number of rows

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
"""


def convert(s: str, num_rows: int) -> str:
    ls = len(s)
    if num_rows <= 1 or ls <= num_rows:
        return s
    if num_rows == 2:
        return s[::2] + s[1::2]
    zs = list(s)
    zz = [zs[:num_rows][::-1]]
    zig, zag = False, True
    p, ic, jc = 1, num_rows, 0
    v = []
    while ic < ls:
        if zig:
            if p == 0:
                v = []
            if p == num_rows - 1 or ic == ls - 1:
                v.append(zs[ic])
                if ic == ls - 1:
                    for _ in range(p + 1, num_rows):
                        v.append(' ')
                    zz.append(v[::-1])
                    break
                else:
                    zz.append(v[::-1])
                p = 1
                zig, zag = False, True
                ic += 1
                continue
            v.append(zs[ic])
            p += 1
        if zag:
            zz.append(list(' ' * p + zs[ic] + ' ' * (num_rows - 1 - p)))
            if p == num_rows - 2 or ic == ls - 1:
                if ic == ls - 1:
                    break
                p = 0
                zig, zag = True, False
                ic += 1
                continue
            p += 1
        ic += 1
    print(zz)
    r = ''
    for i in range(num_rows)[::-1]:
        for j in range(len(zz)):
            x = zz[j][i]
            r += x if x != ' ' else ''
    return r


assert convert('A', 1) == 'A'
assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
assert convert('ABCD', 2) == 'ACBD'
assert convert('ABCDE', 4) == 'ABCED'

print(convert('ABCDE', 4))
