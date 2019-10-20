# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, depth = [], 0
        stack.append((1, root))
        while stack:
            cur, node = stack.pop()
            if node:
                depth = max(depth, cur)
                stack.append((cur+1, node.left))
                stack.append((cur+1, node.right))
        return depth


t = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
t1.left.right = TreeNode(5)
print(t.maxDepth(t1))