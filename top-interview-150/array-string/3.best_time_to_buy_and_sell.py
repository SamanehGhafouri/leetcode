"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    stack = [prices[0]]
    max_diff = 0
    for p in prices:
        if p < stack[-1]:
            stack.pop()
            stack.append(p)
        if p > stack[-1]:
            diff = p - stack[-1]
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    # p = [7, 1, 5, 3, 6, 4]
    p = [7,6,4,3,1]
    print(max_profit(p))
