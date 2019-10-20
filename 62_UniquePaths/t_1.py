class Solution:
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]  # 对于上边界和左边界的点，只有一条路径到达
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


Solution.uniquePaths(7, 3)
