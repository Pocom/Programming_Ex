class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        s_c = Counter(secret)
        g_c = Counter(guess)
        print(s_c, g_c)
        t = sum(i == j for i, j in zip(secret, guess))
        return "{}A{}B".format(t, sum((s_c & g_c).values()) - t)


t = Solution()
t.getHint('1102', '1021')
