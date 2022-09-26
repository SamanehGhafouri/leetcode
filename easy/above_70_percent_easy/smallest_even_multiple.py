"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
"""


def smallest_even_multiple(n: int) -> int:
    if n % 2 == 0 and n < n * 2:
        return n
    return n * 2


if __name__ == '__main__':
    n = 6
    print(smallest_even_multiple(n))
