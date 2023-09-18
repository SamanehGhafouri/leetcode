"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def min_depth_binary_tree(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        depths = []
        while stack:
            node, count = stack.pop()
            new_count = count + 1
            if not node.left and not node.right:
                depths.append(new_count)
            if node.right:
                stack.append((node.right, new_count))
            if node.left:
                stack.append((node.left, new_count))
        return min(depths)


if __name__ == '__main__':
    r = TreeNode(2)
    r.left = TreeNode(7)
    r.right = TreeNode(3)
    r.right.right = TreeNode(4)
    r.right.right.right = TreeNode(5)
    r.right.right.right.right = TreeNode(6)

    s = Solution()
    print(s.min_depth_binary_tree(r))