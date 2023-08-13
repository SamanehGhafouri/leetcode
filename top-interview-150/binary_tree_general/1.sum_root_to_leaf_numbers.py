"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_numbers(self, root: Optional[TreeNode]) -> int:

        stack = [(root, [])]
        nums = []
        while stack:
            node, history = stack.pop()
            if node.right:
                new_history = history + [str(node.val)]
                stack.append((node.right, new_history))
            if node.left:
                new_history = history + [str(node.val)]
                stack.append((node.left, new_history))
            elif node.right is None and node.left is None:
                new_history = history + [str(node.val)]
                nums.append(int("".join(new_history)))
        return sum(nums)

    def sum_numbers_recursion(self, root: Optional[TreeNode]) -> int:
        nums = []

        def dfs(node: Optional[TreeNode], history: List):
            new_history = history + [str(node.val)]
            if node.left:
                dfs(node.left, new_history)
            if node.right:
                dfs(node.right, new_history)
            if node.left is None and node.right is None:
                nums.append(int("".join(new_history)))

        dfs(root, [])
        return sum(nums)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root_node = Solution()
    # print(root_node.sum_numbers(root))
    print(root_node.sum_numbers_recursion(root))
