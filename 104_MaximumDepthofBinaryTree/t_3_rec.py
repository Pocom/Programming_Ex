# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def rec(node, depth):
            if not node: return depth
            return max(rec(node.left, depth + 1), rec(node.right, depth + 1))

        return rec(root, 0)
