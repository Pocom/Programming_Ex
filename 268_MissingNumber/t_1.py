class Solution:
    def missingNumber(self, nums) -> int:
        nums_complete = list(range(0, len(nums)+1))
        return sum(nums_complete) - sum(nums)
