class Solution:
    def minPathSum(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        from sys import maxsize

        dp = [0] + [maxsize] * (len(grid[0]))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        print(dp)

        return dp[-2]


t = Solution()
t.minPathSum([[1,3,1],[1,5,1],[4,2,1]])