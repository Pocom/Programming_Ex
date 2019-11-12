class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        t_ik0, t_ik1 = 0, -sys.maxsize

        for price in prices:
            t_ik0, t_ik1 = max(t_ik0, t_ik1 + price - fee), max(t_ik1, t_ik0 - price)

        return t_ik0
