"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such
that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def has_path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        stack = [(root, root.val)]
        while stack:
            node, history = stack.pop()
            if not node.left and not node.right:
                if history == targetSum:
                    return True
            if node.right:
                stack.append((node.right, history+node.right.val))
            if node.left:
                stack.append((node.left, history+node.left.val))
        return False


if __name__ == '__main__':
    node = TreeNode(5)
    node.left = TreeNode(4)
    node.left.left = TreeNode(11)
    node.left.left.left = TreeNode(7)
    node.left.left.right = TreeNode(2)

    node.right = TreeNode(8)
    node.right.left = TreeNode(13)
    node.right.right = TreeNode(4)
    node.right.right.right = TreeNode(1)

    s = Solution()
    print(s.has_path_sum(node, 22))
