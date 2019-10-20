# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums: return None
        mid = len(nums)//2
        num_root = nums[mid]
        left_nums, right_nums = nums[:mid], nums[mid+1:]
        root = TreeNode(num_root)
        root.left = self.sortedArrayToBST(left_nums) if left_nums else None
        root.right = self.sortedArrayToBST(right_nums) if right_nums else None
        return root


t = Solution()
print(t.sortedArrayToBST([-10,-3,0,5,9]))