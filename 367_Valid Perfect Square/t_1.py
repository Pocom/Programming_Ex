class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s, i = 0, 1
        while s < num:
            s += i
            i += 2
        return True if s == num else False
