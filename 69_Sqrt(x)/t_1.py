class Solution:
    def mySqrt(self, x: int) -> int:
        k = 1.0
        while abs(k * k - x) > 1e-9:
            k = (k + x / k) / 2
        return int(k)


t = Solution()
sqrt_ = t.mySqrt(10)
print(sqrt_)