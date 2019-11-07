class Solution:
    def generateMatrix(self, n):
        """
        :param n: int
        :return: List[List[int]]
        """
        if n == 1: return [[1]]

        ret = [[0 for _ in range(n)] for _ in range(n)]

        num, MAX = 1, n ** 2
        u, d, l, r = 0, n - 1, 0, n - 1

        while num <= MAX:
            for i in range(l, r + 1):
                ret[u][i] = num
                num += 1
            u += 1
            for i in range(u, d + 1):
                ret[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                ret[d][i] = num
                num += 1
            d -= 1
            for i in range(d, u - 1, -1):
                ret[i][l] = num
                num += 1
            l += 1
        print(ret)
        return ret


t = Solution()
t.generateMatrix(3)
