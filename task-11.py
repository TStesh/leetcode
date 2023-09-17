"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container,
such that the container contains the most water. Return the maximum amount of water a container can store. Notice
that you may not slant the container.

Input:
height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.
"""


def max_area(height: [int]) -> int:
    lh = len(height)
    if lh < 2:
        return 0
    max_ar = 0
    max_h = 0
    for i, h in enumerate(height):
        if h > max_h:
            for j in range(i + 1, lh):
                if height[j] > max_h:
                    ar = min(h, height[j]) * (j - i)
                    if ar > max_ar:
                        max_ar = ar
            max_h = h
    return max_ar


def max_area1(height: [int]) -> int:
    lh = len(height)
    if lh < 2:
        return 0
    l, r = 0, lh - 1
    max_ar = 0
    while l < r:
        ar = min(height[l], height[r]) * (r - l)
        if ar > max_ar:
            max_ar = ar
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_ar


assert (max_area1([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
assert (max_area1([1, 1]) == 1)
assert (max_area1([2, 0]) == 0)
assert (max_area1([4, 3, 2, 1, 4]) == 16)
assert (max_area1([1, 2, 1]) == 2)
assert (max_area1([1, 8, 6, 2, 5, 4, 8, 25, 7]) == 49)
assert (max_area1([2, 3, 4, 5, 18, 17, 6]) == 17)
assert (max_area1([1, 3, 2, 5, 25, 24, 5]) == 24)

# print(max_area([1, 8, 6, 2, 5, 4, 8, 25, 7]))
