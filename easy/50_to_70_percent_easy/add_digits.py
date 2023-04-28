"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""


def add_digits(num: int) -> int:
    if num < 10:
        return num
    else:
        result = num // 10 + num % 10
        if result < 10:
            return result
        return add_digits(result)


if __name__ == '__main__':
    n = 38
    print(add_digits(n))
