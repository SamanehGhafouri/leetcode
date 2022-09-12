"""
You are given two 2D integer arrays, items1 and items2, representing two sets of items.
Each array items has the following properties:

items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of
weights of all items with value valuei.

Note: ret should be returned in ascending order by value.
"""
from typing import List


def merge_similar_items(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    item1_dict = {}
    for i in items1:
        item1_dict[i[0]] = i[1]

    result = []
    for j in items2:
        if j[0] in item1_dict:
            result.append([j[0], item1_dict[j[0]] + j[1]])
            del item1_dict[j[0]]
        else:
            result.append(j)
    if len(item1_dict) != 0:
        for k, v in item1_dict.items():
            result.append([k, v])
    return sorted(result)


if __name__ == '__main__':
    li_1 = [[1, 3], [2, 2]]
    li_2 = [[7, 1], [2, 2], [1, 4]]
    print(merge_similar_items(li_1, li_2))
