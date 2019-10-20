# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = [root]
        cnt = 0
        if not root:
            return 0
        while queue:
            next_queue = list()
            for node in queue:
                if not node: continue
                next_queue.append(node.left)
                next_queue.append(node.right)
            cnt += 1
            if not next_queue:
                cnt -= 1
            queue = next_queue
        return cnt


t = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
t1.left.right = TreeNode(5)
print(t.maxDepth(t1))