# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]

        queue, ret = [root], []
        while queue:
            next_queue = []
            mmax = queue[0].val
            for node in queue:
                mmax = max(mmax, node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            ret.append(mmax)
            queue = next_queue

        return ret
