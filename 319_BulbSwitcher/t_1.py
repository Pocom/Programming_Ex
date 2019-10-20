class Solution:
    def bulbSwitch(self, n: int) -> int:
        if not n: return 0
        elif n in [1, 2]: return 1

        bulb = [1] * n

        for i in range(2, n+1):
            mul = 1
            while i*mul <= n:
                bulb[i*mul-1] = 0 if bulb[i*mul-1] else 1
                mul += 1

        return sum(bulb)
