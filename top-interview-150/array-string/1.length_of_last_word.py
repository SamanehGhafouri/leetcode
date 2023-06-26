"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])


if __name__ == '__main__':
    string = "   fly me   to   the moon  "
    print(length_of_last_word(string))
