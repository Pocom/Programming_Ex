class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        lenOfX = len(str(x))
        if lenOfX == 1:
            return True
        digit_1 = digit_2 = ''
        x_1 = x_2 = x
        for i in range(int(lenOfX/2)):
            digit_1 += str(x_1 % 10)
            x_1 = int(x_1 / 10)
            print('digit_1: ', digit_1)
        for i in range(int(lenOfX/2)):
            digit_2 += str(int(x_2 / (10**(lenOfX-1))))
            x_2 = int(x_2 % (10**(lenOfX-1)))
            lenOfX -= 1
            print('digit_2: ', digit_2)
        if digit_1 == digit_2:
            return True
        else:
            return False


# testing
t = Solution()
print(t.isPalindrome(100))
