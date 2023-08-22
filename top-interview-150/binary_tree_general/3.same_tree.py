"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1.left and not node2.left or not node1.left and node2.left:
                return False
            if node1.right and not node2.right or not node1.right and node2.right:
                return False
            if node1.right and node2.right:
                if node1.right.val != node2.right.val:
                    return False
                stack.append((node1.right, node2.right))
            if node1.left and node2.left:
                if node1.left.val != node2.left.val:
                    return False
                stack.append((node1.left, node2.left))
        return True


if __name__ == '__main__':
    root_1 = TreeNode(1)
    root_2 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_2.right = TreeNode(2)

    s = Solution()
    print(s.is_same_tree(root_1, root_2))
