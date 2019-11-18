class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0 if len(nums) == 1 or nums[0] >= nums[1] else 1
        elif nums[0] > nums[1]:
            return 0
        for i in range(1, len(nums)):
            if i + 1 > len(nums) - 1: break
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
