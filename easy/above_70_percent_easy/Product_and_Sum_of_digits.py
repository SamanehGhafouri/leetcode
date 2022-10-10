"""
Subtract the product and sum of digits of an integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


def subtract_product_and_sum(n: int) -> int:
    product = 1
    sum_digits = 0
    for num in str(n):
        product *= int(num)
        sum_digits += int(num)
    return product - sum_digits


if __name__ == '__main__':
    print(subtract_product_and_sum(4421))
