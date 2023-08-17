"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepest_leaves_sum(self, root: Optional[TreeNode]):
        stack = [(root, 0)]
        leaves_length = []
        while stack:
            node, length = stack.pop()
            if node.right:
                new_length = length + 1
                stack.append((node.right, new_length))
            if node.left:
                new_length = length + 1
                stack.append((node.left, new_length))
            elif not node.right and not node.left:
                new_length = length + 1
                leaves_length.append((new_length, node.val))
        max_h = max(leaves_length, key=lambda item: item[0])[0]
        result_sum = 0
        for tup in leaves_length:
            if tup[0] == max_h:
                result_sum += tup[1]
        return result_sum


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(9)
    root.right = TreeNode(8)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(5)
    root_node = Solution()
    print(root_node.deepest_leaves_sum(root))
