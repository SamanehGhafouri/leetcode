"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight,
so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very
much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if
she only eats n / 2 of them.
"""
from typing import List


def distribute_candies(candy_type: List[int]) -> int:
    len_set = len(set(candy_type))
    num_candies_allowed = len(candy_type) // 2
    if len_set <= num_candies_allowed:
        return len_set
    return num_candies_allowed


if __name__ == '__main__':
    candy_type = [1, 1, 2, 2, 3, 3]
    print(distribute_candies(candy_type))
