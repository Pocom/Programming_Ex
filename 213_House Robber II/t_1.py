class Solution:
    def rob(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 0: return 0
        elif length == 1: return nums[0]
        elif length == 2: return max(nums[0], nums[1])

        def rob_action(nums):
            length = len(nums)
            dp = [0 for _ in range(length)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, length):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp

        nums1 = nums[1:]
        dp1 = rob_action(nums1)

        nums2 = nums[:-1]
        dp2 = rob_action(nums2)

        return max(dp1[-1], dp2[-1])
