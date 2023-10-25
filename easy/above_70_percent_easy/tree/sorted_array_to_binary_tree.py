"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def binary_search_node(nums, start, end):
        if start <= end:
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = binary_search_node(nums, start, mid - 1)
            node.right = binary_search_node(nums, mid + 1, end)
            return node

    return binary_search_node(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(sortedArrayToBST(nums))
