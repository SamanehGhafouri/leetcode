"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i^th customer has in the
 j^th bank. Return the wealth that the richest customer has.

 A customer's wealth is the amount of money they have in all their bank accounts.
  The richest customer is the customer that has the maximum wealth.
"""
from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    wealth = []

    for customer in range(len(accounts)):
        wealth.append(sum(accounts[customer]))
    return max(wealth)


if __name__ == '__main__':
    accounts_li = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(maximum_wealth(accounts_li))
