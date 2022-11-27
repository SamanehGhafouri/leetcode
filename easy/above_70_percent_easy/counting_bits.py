"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""
from typing import List


def count_bits(n: int) -> List[int]:
    result = []
    for i in range(n + 1):
        result.append(bin(i)[2::].count('1'))
    return result


if __name__ == '__main__':
    n = 5
    print(count_bits(n))
