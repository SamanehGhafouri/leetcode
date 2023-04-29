"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    while len(stones) >= 1:
        stones.sort()
        if len(stones) == 1:
            return stones.pop()
        max_num = stones.pop()
        second_max_num = stones.pop()
        diff = max_num - second_max_num
        if diff != 0:
            stones.append(diff)
    return 0


if __name__ == '__main__':
    stones_li = [2, 7, 4, 1, 8, 1]
    print(last_stone_weight(stones_li))