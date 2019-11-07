import sys


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if k >= len(prices) >> 1:
            t_ik0, t_ik1 = 0, -sys.maxsize

            for price in prices:
                t_ik0, t_ik1 = max(t_ik0, t_ik1 + price), max(t_ik1, t_ik0 - price)

            return t_ik0

        t_ik0 = [0] * (k + 1)
        t_ik1 = [-sys.maxsize] * (k + 1)

        for price in prices:
            for j in range(k, 0, -1):
                t_ik0[j] = max(t_ik0[j], t_ik1[j] + price)
                t_ik1[j] = max(t_ik1[j], t_ik0[j - 1] - price)
        print(t_ik0)
        return t_ik0[k]


t = Solution()
k = 4
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
t.maxProfit(k, prices)
