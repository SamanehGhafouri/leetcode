"""
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
"""

def sum_of_multiples(n: int) -> int:
    sum_of_nums = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            sum_of_nums += i
    return sum_of_nums

if __name__ == '__main__':
    n = 10
    print(sum_of_multiples(n))