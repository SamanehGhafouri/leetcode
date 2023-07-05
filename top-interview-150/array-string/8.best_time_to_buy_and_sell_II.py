"""
Medium problem:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the
stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    max_p = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            max_p += prices[i + 1] - prices[i]
    return max_p


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [1, 2, 3, 4, 5]
    # prices = [4, 3, 2, 1]
    # prices = [6,1,3,2,4,7]
    print(max_profit(prices))
