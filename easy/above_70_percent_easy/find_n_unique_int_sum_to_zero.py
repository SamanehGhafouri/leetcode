"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""
from typing import List


def sum_zero(n: int) -> List[int]:
    result = []
    for num in range(n // 2):
        result.append(num + 1)
        result.append(-num - 1)

    if n % 2 != 0:
        result.append(0)
    return result


if __name__ == '__main__':
    num_n = 5
    print(sum_zero(num_n))
