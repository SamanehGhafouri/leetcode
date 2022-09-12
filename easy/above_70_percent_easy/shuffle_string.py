"""
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position
moves to indices[i] in the shuffled string.

Return the shuffled string.
"""
from typing import List


def restore_string(s: str, indices: List[int]) -> str:
    li = []
    for i in range(len(indices)):
        tuple_li = [indices[i], s[i]]
        li.append(tuple_li)
    sorted_li = sorted(li)
    str_li = []
    for i in range(len(sorted_li)):
        str_li.append(sorted_li[i][1])
    return "".join(str_li)


if __name__ == '__main__':
    li_indices = [4, 5, 6, 7, 0, 2, 1, 3]
    st = "codeleet"
    print(restore_string(st, li_indices))
