class Solution:
    def coinChange(self, coins, amount):
        """
        :param coins: List[int]
        :param amount: int
        :return: int
        """
        import sys
        if not amount: return 0
        ans = sys.maxsize
        for coin in coins:
            if amount - coin < 0: continue
            sub_problem = self.coinChange(coins, amount - coin)
            if sub_problem == -1: continue
            ans = min(ans, sub_problem + 1)
        return -1 if ans == sys.maxsize else ans


t = Solution()

coins = [1,2,5]
amount = 11
t.coinChange(coins, amount)