class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1: return 0
        print("N = {}, K = {}".format(N, K))
        return (1 - K % 2) ^ self.kthGrammar(N - 1, (K + 1) // 2)


t = Solution()
t.kthGrammar(4, 4)
