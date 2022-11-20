"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
"""


def repeated_character(s: str) -> str:
    dict_s = {}
    for ch in s:
        if ch not in dict_s:
            dict_s[ch] = 1
        else:
            return ch


if __name__ == '__main__':
    string = "abcdd"
    print(repeated_character(string))
