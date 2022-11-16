"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(reverse_string(s))
