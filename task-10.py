"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


def repl_dots(s: str, p: str) -> str:
    xs = list(s)
    k = 0
    while 1:
        k_new = p.find('.', k)
        if k_new == -1:
            break
        xs[k_new] = '.'
        k = k_new + 1
    return ''.join(xs)


def is_match(s: str, p: str) -> bool:
    if '.*' in p:
        return True
    is_stars = '*' in p
    is_dots = '.' in p
    if not is_stars and not is_dots:
        return p in s if len(s) >= len(p) else False
    if is_dots:
        s = repl_dots(s, p)
    if not is_stars:
        return p == s
    # борьба со звездочками

    return True


print(is_match('bbbd', '.b.d'))

