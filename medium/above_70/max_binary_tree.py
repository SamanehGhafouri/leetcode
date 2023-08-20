"""
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    max_val = max(nums)
    max_indx = nums.index(max_val)
    left_nodes = nums[:max_indx]
    right_nodes = nums[max_indx + 1:]
    root = TreeNode(max_val)
    stack = [(root, right_nodes, left_nodes)]

    while stack:
        node, right_ch, left_ch = stack.pop()
        if right_ch:
            max_value = max(right_ch)
            max_index = right_ch.index(max_value)
            node.right = TreeNode(max_value)
            new_right_ch = right_ch[max_index + 1:]
            new_left_ch = right_ch[:max_index]
            stack.append((node.right, new_right_ch, new_left_ch))
        if left_ch:
            max_value = max(left_ch)
            max_index = left_ch.index(max_value)
            node.left = TreeNode(max_value)
            new_right_ch = left_ch[max_index + 1:]
            new_left_ch = left_ch[:max_index]
            stack.append((node.left, new_right_ch, new_left_ch))

    return root


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    # nums = [3,2,1]
    print(constructMaximumBinaryTree(nums))
