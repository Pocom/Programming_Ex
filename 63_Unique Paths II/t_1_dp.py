class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :param obstacleGrid: List[List[int]]
        :return: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # dp = [[1] * col] + [[1] + [0] * (col - 1) for _ in range(row-1)]
        dp = [[1] + [0] * (col-1)] + [[0]*col for _ in range(row-1)]
        for i in range(1, row):
            if obstacleGrid[i][0] in [1]:
                break
            else:
                dp[i][0] = dp[i-1][0]
        print(dp)
        for i in range(1, col):
            if obstacleGrid[0][i] in [1]:
                break
            else:
                dp[0][i] = dp[0][i-1]
        print(dp)
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] in [1]:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]


t = Solution()
t.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
