"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    li = []
    for i, j in zip(nums[:n], nums[n:]):
        li.append(i)
        li.append(j)
    return li


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(shuffle(nums, n))
