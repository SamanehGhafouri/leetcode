"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer
appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""
import collections


def find_duplicates(nums):
    return [k for k, v in collections.Counter(nums).items() if v >= 2]

if __name__ == '__main__':
    n = [4,3,2,7,8,2,3,1]
    print(find_duplicates(n))