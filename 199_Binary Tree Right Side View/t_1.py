# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue, ret = [root], []
        while queue:
            next_queue, num, mark = [], 0, False
            for node in queue:
                if node:
                    next_queue.extend([node.left, node.right])
                    num, mark = node.val, True
            if mark: ret.append(num)
            queue = next_queue
        return ret