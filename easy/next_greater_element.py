"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the
same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""
from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    dict_greater = {}

    stack = [nums2[0]]
    for num in nums2[1:]:
        if num < stack[-1]:
            stack.append(num)
        while len(stack) > 0 and stack[-1] < num:
            dict_greater[stack.pop()] = num
        stack.append(num)

    while len(stack) > 0:
        dict_greater[stack.pop()] = -1

    return [dict_greater[j] for j in nums1 if j in dict_greater]


if __name__ == '__main__':
    # arr1 = [1, 3, 5, 2, 4]
    # arr2 = [6, 5, 4, 3, 2, 1, 7]
    # arr1 = [4,1,2]
    # arr2 = [1,3,4,2]
    arr1 = [137, 59, 92, 122, 52, 131, 79, 236, 94, 171, 141, 86, 169, 199]
    arr2 = [137, 59, 92, 122, 52, 131, 79, 236, 94, 171, 141, 86, 169, 199]
    print(next_greater_element(arr1, arr2))
