class Solution:
    def fib(self, N: int) -> int:
        if not N: return 0
        if N == 1: return 1

        def helper(MAX):
            n, a, b = 1, 0, 1
            while n < MAX:
                a, b = b, a + b
                yield b
                n += 1

        for i in helper(N):
            ret = i
        return ret


t = Solution()
num0 = t.fib(5)
print(num0)
