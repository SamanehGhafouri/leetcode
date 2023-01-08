"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    inorder(root, result)
    return result


def inorder(root: Optional[TreeNode], result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(inorderTraversal(root))
