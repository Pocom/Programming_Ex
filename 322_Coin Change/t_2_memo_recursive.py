class Solution:
    def coinChange(self, coins, amount):
        """
        :param coins: List[int]
        :param amount: int
        :return: int
        """
        import sys
        def helper(coins, amount, memo):
            if not amount: return 0
            if memo[amount] != -2: return memo[amount]
            ans = sys.maxsize
            for coin in coins:
                if amount - coin < 0: continue
                sub_problem = helper(coins, amount - coin, memo)
                if sub_problem == -1: continue
                ans = min(ans, sub_problem + 1)

            memo[amount] = -1 if ans == sys.maxsize else ans
            print(memo)
            return memo[amount]

        memo = [-2] * (amount + 1)
        return helper(coins, amount, memo)


t = Solution()

coins = [1,2,5]
amount = 100
t.coinChange(coins, amount)