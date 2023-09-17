"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


def romanToInt(s: str) -> int:
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    t = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    len_s = len(s)
    if len_s == 1:
        return d[s]
    if len_s == 2 and s in t:
        return t[s]
    n, i = 0, 0
    while i < len_s:
        v = s[i]
        if v in ('I', 'X', 'C'):
            if i + 1 < len_s:
                w = v + s[i + 1]
                if w in t:
                    n += t[w]
                    i += 2
                    continue
        n += d[v]
        i += 1
    return n


print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))

"""
x = list(set(num1).union(set(num2)))
x.sort()

lx = len(x)
lm = lx // 2

mediana = x[lm] if lx % 2 else (x[lm - 1] + x[lm]) / 2

print(mediana)
"""