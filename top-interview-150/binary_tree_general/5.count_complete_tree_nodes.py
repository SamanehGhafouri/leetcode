"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a
complete binary tree, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        count = 1
        while stack:
            node = stack.pop()
            if node.right:
                count += 1
                stack.append(node.right)
            if node.left:
                count += 1
                stack.append(node.left)
        return count


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)
    r.right = TreeNode(3)
    r.right.left = TreeNode(6)

    s = Solution()
    print(s.count_nodes(r))
