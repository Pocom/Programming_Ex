# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        queue = [root]
        ret = []
        while queue:
            next_queue = []
            current_nums = []
            for node in queue:
                if node:
                    current_nums.append(node.val)
                    next_queue.extend([node.left, node.right])
            queue = next_queue
            if current_nums:
                ret.append(current_nums)
        return ret
