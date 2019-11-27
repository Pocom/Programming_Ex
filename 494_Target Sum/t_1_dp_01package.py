from typing import List


class Solution:

    # 01背包
    # target =  sum(P) - sum(N)
    # P 为正子集 N 为负子集

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1): dp[j] += dp[j - num]
        return dp[P]


t = Solution()
nums = [1, 1, 1, 1, 1]
s = 3
t.findTargetSumWays(nums, s)
