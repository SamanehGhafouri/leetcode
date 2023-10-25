"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    postorder(root, result)
    return result

def postorder(root: Optional[TreeNode], result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.val)

if __name__ == '__main__':
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)
    print(postorderTraversal(r))
