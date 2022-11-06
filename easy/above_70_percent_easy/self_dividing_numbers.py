"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
"""
from typing import List


def self_dividing_numbers(left: int, right: int) -> List[int]:
    list_dividing_num = []
    for num in range(left, right + 1):
        if "0" not in str(num):
            count = 0
            for n in str(num):
                if num % int(n) == 0:
                    count += 1
            if count == len(str(num)):
                list_dividing_num.append(num)
    return list_dividing_num


if __name__ == '__main__':
    l = 47
    r = 85
    print(self_dividing_numbers(l, r))
