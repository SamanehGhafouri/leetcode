"""

"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for num in nums:
        result += [item + [num] for item in result]
    return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets(nums))
