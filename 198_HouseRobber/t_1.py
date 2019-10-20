class Solution:
    def rob(self, nums) -> int:
        last = now = 0
        # DP问题
        for i in nums: last, now = now, max(last + i, now)
        return now

