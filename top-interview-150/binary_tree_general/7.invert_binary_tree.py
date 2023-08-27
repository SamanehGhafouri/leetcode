"""
Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root


if __name__ == '__main__':
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right = TreeNode(3)
    s = Solution()
    print(s.invert_tree(node))
