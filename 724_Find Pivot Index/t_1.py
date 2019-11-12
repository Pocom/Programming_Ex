class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_, left = sum(nums), 0
        for i in range(len(nums)):
            if left * 2 + nums[i] == sum_:
                return i
            left += nums[i]
        return -1
