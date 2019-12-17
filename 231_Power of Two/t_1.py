class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if not n: return False

        while True:
            if n == 1:
                return True
            if n % 2:
                return False
            n /= 2
