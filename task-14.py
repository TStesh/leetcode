"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longest_common_prefix(strs: [str]) -> str:
    pref = ''
    if len(strs) == 0:
        return pref
    if len(strs) == 1:
        return strs[0]
    sorted_strs = sorted(strs)
    base = sorted_strs[0]
    found = True
    for i, c in enumerate(base):
        for t in sorted_strs[1:]:
            if t[i] != c:
                found = False
                break
        if found:
            pref += c
        else:
            break
    return pref


assert (longest_common_prefix(["a"]) == 'a')
assert (longest_common_prefix(["flower", "flow", "flight"]) == 'fl')
assert (longest_common_prefix(["dog", "racecar", "car"]) == '')
