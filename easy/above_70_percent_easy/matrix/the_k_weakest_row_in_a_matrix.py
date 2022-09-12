"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""
from typing import List


def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    dict_num_soldiers = {}
    count_soldiers = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                count_soldiers += 1
        dict_num_soldiers[i] = count_soldiers
        count_soldiers = 0

    sorted_dict = {key: val for key, val in sorted(dict_num_soldiers.items(), key=lambda item: item[1])}
    list_k_weakest = []
    for key, val in sorted_dict.items():
        if len(list_k_weakest) != k:
            list_k_weakest.append(key)
    return list_k_weakest


if __name__ == '__main__':
    matrix_a = [[1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0]]
    k_a = 2
    print(k_weakest_rows(matrix_a, k_a))
