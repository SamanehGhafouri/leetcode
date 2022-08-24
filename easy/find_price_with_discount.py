"""
Given the array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop, if you buy the ith item,
then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i],
otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering
the special discount.
"""
from typing import List


def final_prices(prices: List[int]) -> List[int]:
    prices_copy = prices
    for i in range(len(prices)):
        smaller_prices = []
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j]:
                smaller_prices.append(prices[j])
        if len(smaller_prices) >= 1:
            prices_copy[i] = prices[i] - smaller_prices[0]
    return prices_copy


if __name__ == '__main__':
    li = [8, 4, 6, 2, 3]
    print(final_prices(li))
