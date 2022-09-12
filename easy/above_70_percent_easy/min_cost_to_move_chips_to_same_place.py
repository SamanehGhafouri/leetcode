"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of
the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
"""

from typing import List


def min_cost_to_move_chips(position: List[int]) -> int:
    even_count = 0
    odd_count = 0
    for i in position:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return min(even_count, odd_count)


if __name__ == '__main__':
    arr = [2, 2, 2, 3, 3]
    print(min_cost_to_move_chips(arr))
