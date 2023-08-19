"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique
ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in.
For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers,
return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""

from typing import List


def group_the_people(group_size: List[int]) -> List[List[int]]:
    dict_group_size = {}
    for i in range(len(group_size)):
        dict_group_size[i] = group_size[i]

    sorted_dict_by_v = dict(sorted(dict_group_size.items(), key=lambda item: item[1]))

    result = []
    group_list = []
    val = sorted_dict_by_v[next(iter(sorted_dict_by_v))]
    for num, l in sorted_dict_by_v.items():
        if len(group_list) < l == val:
            group_list.append(num)
            val = l
        else:
            result.append(group_list)
            group_list = [num]
            val = l
    if len(group_list) != 0:
        result.append(group_list)
    return result


if __name__ == '__main__':
    group_s = [2, 1, 3, 3, 3, 2]
    print(group_the_people(group_s))
