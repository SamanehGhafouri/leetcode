"""
Given a string s and a character letter, return the percentage of characters in s that
equal letter rounded down to the nearest whole percent.
"""


def percentage_letter(s: str, letter: str) -> int:
    return s.count(letter) * 100 // len(s)


if __name__ == '__main__':
    s = "foobar"
    letter = "o"
    print(percentage_letter(s, letter))
