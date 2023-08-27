"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
import collections
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        stack = collections.deque([root.left, root, root.right])
        while len(stack) > 1:
            right_node = stack.pop()
            left_node = stack.popleft()
            if not right_node and not left_node:
                continue
            if not right_node and left_node:
                return False
            if not left_node and right_node:
                return False
            if right_node.val != left_node.val:
                return False
            stack.append(right_node.left)
            stack.appendleft(left_node.right)
            stack.append(right_node.right)
            stack.appendleft(left_node.left)
        return True


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(3)
    r.left.right = TreeNode(4)

    r.right = TreeNode(2)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(3)

    s = Solution()
    print(s.is_symmetric(r))
