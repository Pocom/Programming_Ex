class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        i = abs(n)
        while i != 0:
            if i % 2 != 0:
                ans *= x
            x *= x
            i //= 2

        return ans if n > 0 else 1 / ans
