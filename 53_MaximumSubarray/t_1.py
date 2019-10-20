class Solution:
    def maxSubArray(self, nums) -> int:
        sum = 0
        ans = nums[0]
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans
