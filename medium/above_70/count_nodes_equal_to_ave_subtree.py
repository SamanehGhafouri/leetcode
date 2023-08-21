"""
Given the root of a binary tree, return the number of nodes where the value of the node is
equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def average_subtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, 0  # sum_nodes_val, sum_chs
            sum_node_val_l, sum_chs_l = dfs(node.left)
            sum_node_val_r, sum_chs_r = dfs(node.right)
            sum_node_val = sum_node_val_l + sum_node_val_r + node.val
            num_nodes = sum_chs_r + sum_chs_l + 1
            avg = sum_node_val // num_nodes
            if avg == node.val:
                nonlocal count
                count += 1
            return sum_node_val, num_nodes

        dfs(root)
        return count


if __name__ == '__main__':
    r = TreeNode(4)
    r.left = TreeNode(8)
    r.left.left = TreeNode(0)
    r.left.right = TreeNode(1)
    r.right = TreeNode(5)
    r.right.right = TreeNode(6)

    n = Solution()
    print(n.average_subtree(r))
