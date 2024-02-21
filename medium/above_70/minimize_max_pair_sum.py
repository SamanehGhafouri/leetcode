"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.
"""
from typing import List


def min_pair_sum(nums: List[int]) -> int:
    nums.sort()
    i = 0
    j = len(nums) - 1
    li_sum = []
    while i < j:
        li_sum.append(nums[i] + nums[j])
        i += 1
        j -= 1
    return max(li_sum)


if __name__ == '__main__':
    nums = [4, 1, 5, 1, 2, 5, 1, 5, 5, 4]
    print(min_pair_sum(nums))
