"""
There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies,
denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""
from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    max_candies_a_kid_have = max(candies)
    diff_of_max_candies_extra_candies = max_candies_a_kid_have - extra_candies
    output_list = []

    for candy in candies:
        if candy >= diff_of_max_candies_extra_candies:
            output_list.append(True)
        else:
            output_list.append(False)
    return output_list


if __name__ == '__main__':
    candies_list = [4, 2, 1, 1, 2]
    ext_candies = 1
    candies_list_two = [2, 3, 5, 1, 3]
    ext_candies_two = 3
    print(kids_with_candies(candies_list, ext_candies))
