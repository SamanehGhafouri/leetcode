"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        nums = []
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        while stack:
            node, count = stack.pop()
            nums.append(count)
            if node.right:
                stack.append((node.right, count + 1))
            if node.left:
                stack.append((node.left, count + 1))
        return max(nums)


if __name__ == '__main__':
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)

    s = Solution()
    print(s.max_depth(node))
