"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""
from typing import List


def find_matrix(nums: List[int]) -> List[List[int]]:
    matrix = []
    while len(nums) != 0:
        m = []
        for num in nums[::-1]:
            if num not in set(m):
                m.append(num)
                nums.remove(num)
        matrix.append(m)
    return matrix

if __name__ == '__main__':
    nums = [1, 3, 4, 1, 2, 3, 1]
    print(find_matrix(nums))
