"""
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
"""


def count_digits(num: int) -> int:
    count = 0
    for val in str(num):
        if num % int(val) == 0:
            count += 1
    return count


if __name__ == '__main__':
    n = 1248
    print(count_digits(n))
