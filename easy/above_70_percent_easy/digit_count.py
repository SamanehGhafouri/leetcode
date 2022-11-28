"""
You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num,
otherwise return false.
"""


def digit_count(num: str) -> bool:
    count = 0
    for i in range(len(num)):
        if num.count(str(i)) == int(num[i]):
            count += 1
    if len(num) == count:
        return True
    return False


if __name__ == '__main__':
    num = "5210010007"
    print(digit_count(num))
