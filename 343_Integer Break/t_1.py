class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2: return dp[n]
        dp += [0] * (n - 2)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[n]
