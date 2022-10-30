"""
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
"""


def count_asterisks(s: str) -> int:

    c_asterisks = 0
    count_bars = 0
    for ch in s:
        if count_bars == 0 and ch =="*":
            c_asterisks += 1
        if count_bars == 0 and ch == "|":
            count_bars += 1
        elif count_bars != 0 and ch == "|":
            count_bars -= 1
    return c_asterisks


if __name__ == '__main__':
    st = "*||*|||||*|*|***||*||***|"
    s = "l|*e*et|c**o|*de|"
    print(count_asterisks(s))
