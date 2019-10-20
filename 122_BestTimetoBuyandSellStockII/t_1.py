class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for day in range(len(prices) - 1):
            differ = prices[day + 1] - prices[day]
            if differ > 0:
                profit += differ
        return profit


t = Solution()
print(t.maxProfit([7,1,5,3,6,4]))