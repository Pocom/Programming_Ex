class Solution:
    def numSquares(self, n: int) -> int:
        import sys
        dp = [0, 1, 2]
        if n <= 2: return dp[n]
        dp += [sys.maxsize] * (n - 2)
        for i in range(2, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[n]


t = Solution()
t.numSquares(13)
