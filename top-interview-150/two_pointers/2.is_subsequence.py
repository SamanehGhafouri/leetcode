"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


def is_subsequence(s: str, t: str) -> bool:
    if len(s) == len(t) and s == t:
        return True

    i = 0
    j = 0
    temp = []
    while len(t) > i:
        if j == len(s):
            return "".join(temp) == s
        if t[i] == s[j]:
            temp.append(t[i])
            i += 1
            j += 1
        else:
            i += 1
    return "".join(temp) == s


if __name__ == '__main__':
    items = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("abc", "abc", True)
    ]

    for item in items:
        print(item[2] == is_subsequence(item[0], item[1]))
