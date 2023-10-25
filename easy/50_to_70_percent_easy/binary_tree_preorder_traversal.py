"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    li = []
    preorder(root, li)
    return li

def preorder(root: Optional[TreeNode], li):
    if root:
        li.append(root.val)
        preorder(root.left, li)
        preorder(root.right, li)


if __name__ == '__main__':
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)
    print(preorderTraversal(r))