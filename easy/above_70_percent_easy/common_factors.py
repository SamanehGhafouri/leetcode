"""
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
"""
from math import gcd


def common_factors(a: int, b: int) -> int:
    count_common_factors = 0
    for n in range(1, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            count_common_factors += 1
    return count_common_factors


if __name__ == '__main__':
    a = 12
    b = 6
    print(common_factors(a, b))
