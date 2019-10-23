class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :param dungeon: List[List[int]]
        :return: int
        """
        from sys import maxsize
        # 记录峰值
        m, n = len(dungeon), len(dungeon[0])
        dp = [0] + [-maxsize] * n
        # _min = 0
        for i in range(m):
            for j in range(n):
                dp[j] = max(dp[j], dp[j-1]) + dungeon[i][j]
            print(dp)

        _min = min(dp)
        return -_min + 1


t = Solution()
t.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])