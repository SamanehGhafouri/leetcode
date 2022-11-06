"""
Given an integer n (in base 10) and a base k, return the sum of the digits of n after
converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
"""


def sum_base(n: int, k: int) -> int:
    remainders = []
    if (n // k) < k:
        remainders.append(n % k)
        remainders.append(n//k)
    else:
        while (n // k) >= 1:
            remainders.append(n % k)
            if (n // k) < k:
                remainders.append(n // k)
            n = n // k
    return sum(remainders)


if __name__ == '__main__':
    n = 42
    k = 2
    print(sum_base(n, k))
