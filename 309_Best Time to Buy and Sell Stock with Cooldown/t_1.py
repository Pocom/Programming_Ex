class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t_ik0, t_ik1, t_ik0_pre = 0, -sys.maxsize, 0

        for price in prices:
            t_ik0_pre, t_ik0, t_ik1 = t_ik0, max(t_ik0, t_ik1 + price), max(t_ik1, t_ik0_pre - price)

        return t_ik0
