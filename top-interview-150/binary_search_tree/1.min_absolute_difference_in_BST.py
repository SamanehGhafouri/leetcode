"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any
two different nodes in the tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        nodes_val = [root.val]
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                nodes_val.append(node.right.val)
                stack.append(node.right)
            if node.left:
                nodes_val.append(node.left.val)
                stack.append(node.left)

        nodes_val.sort()
        min_diff = abs(nodes_val[0] - nodes_val[1])
        for i in range(2, len(nodes_val)):
            diff = abs(nodes_val[i] - nodes_val[i - 1])
            if diff <= min_diff:
                min_diff = diff
        return min_diff


if __name__ == '__main__':
    r = TreeNode(543)
    r.left = TreeNode(384)
    r.left.right = TreeNode(445)
    r.right = TreeNode(652)
    r.right.right = TreeNode(699)

    s = Solution()
    print(s.get_minimum_difference(r))
