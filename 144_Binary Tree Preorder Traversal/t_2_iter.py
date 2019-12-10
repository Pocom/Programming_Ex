# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        ret = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            ret.append(node.val)
            if node.right:
                queue.insert(0, node.right)
            if node.left:
                queue.insert(0, node.left)

        return ret
