"""
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""
from typing import List


def num_rescue_boats(people: List[int], limit: int) -> int:
    people.sort()
    left = 0
    right = len(people) - 1
    count_boats = 0

    while left <= right:
        if len(people) == 1:
            count_boats += 1
        if people[right] == limit:
            count_boats += 1
            right -= 1
        elif people[right] < limit:
            if people[left] + people[right] == limit or people[left] + people[right] < limit:
                count_boats += 1
                left += 1
                right -= 1
            else:
                count_boats += 1
                right -= 1
    return count_boats


if __name__ == '__main__':
    p = [3, 2, 2, 1]
    lim = 3
    print(num_rescue_boats(p, lim))
