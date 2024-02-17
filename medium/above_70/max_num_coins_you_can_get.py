"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
"""
from typing import List


def max_coin(piles: List[int]) -> int:
    piles.sort()
    total = 0
    li = []
    i = 0
    j = len(piles) - 1
    while i < j:
        li.append(piles[j])
        li.append(piles[j - 1])
        li.append(piles[i])
        j -= 2
        i += 1
    while li:
        li.pop()
        total += li.pop()
        li.pop()
    return total


if __name__ == '__main__':
    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    print(max_coin(piles))
