class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c: return True
        from math import sqrt
        for i in range(1, int(sqrt(c)) + 1):
            rest = c - i ** 2
            if int(sqrt(rest)) ** 2 == rest:
                return True
        return False
