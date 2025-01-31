# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node, nums):
            if not node: return
            inorder(node.left, nums)
            nums.append(node.val)
            inorder(node.right, nums)

        nums = []
        inorder(root, nums)
        return nums[k - 1]
