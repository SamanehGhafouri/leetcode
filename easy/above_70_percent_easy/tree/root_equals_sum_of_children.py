"""
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_tree(self, root: Optional[TreeNode]) -> bool:
        if root.val == (root.right.val + root.left.val):
            return True
        return False


if __name__ == '__main__':
    left_child = TreeNode(4, None, None)
    right_child = TreeNode(6, None, None)
    root = TreeNode(10, left_child, right_child)
    solution = Solution()
    result = solution.check_tree(root)
    print(result)
