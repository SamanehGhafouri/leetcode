"""
Split a string in Balanced Strings.
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
"""


def balanced_string_split(s: str) -> int:
    sum_balanced = 0
    count = 0
    for ch in s:
        if ch == "R":
            sum_balanced += 1
        else:
            sum_balanced -= 1
        if sum_balanced == 0:
            count += 1
    return count


if __name__ == '__main__':
    st = "RLRRRLLRLL"
    print(balanced_string_split(st))
