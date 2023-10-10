"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of
all the values of the nodes in the tree.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        nums = [root.val]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                nums.append(node.right.val)
            if node.left:
                stack.append(node.left)
                nums.append(node.left.val)
        nums.sort()
        return nums[k - 1]


if __name__ == '__main__':
    k = 1
    r = TreeNode(3)
    r.left = TreeNode(1)
    r.right = TreeNode(4)
    r.left.right = TreeNode(2)

    s = Solution()
    print(s.kthSmallest(r, k))
