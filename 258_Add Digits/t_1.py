class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 <= 0:
            return num
        else:
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10
            next_num = sum(digits)
            return self.addDigits(next_num)


t = Solution()
print(t.addDigits(11))
