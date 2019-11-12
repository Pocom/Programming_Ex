class Solution:
    def plusOne(self, digits):

        carry, ret = 1, []
        for digit in digits[::-1]:
            new_digit = digit + carry
            if new_digit >= 10:
                ret.insert(0, new_digit - 10)
                carry = 1
            else:
                ret.insert(0, new_digit)
                carry = 0
        if carry == 1:
            ret.insert(0, 1)

        return ret


t = Solution()
t.plusOne([1, 2, 3])
