"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
import re


def is_palindrome(s: str) -> bool:
    alpha_num_only = re.sub('[^A-Za-z0-9]+', '', s)
    return alpha_num_only.lower() == alpha_num_only.lower()[::-1]


if __name__ == '__main__':
    s = "dog 1a, (1) god"
    print(is_palindrome(s))
