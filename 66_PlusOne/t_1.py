class Solution:
    def plusOne(self, digits):
        if not digits:
            return [1]
        print(digits)
        print(type(digits))
        strNum = ''.join([str(x) for x in digits])
        intNum = int(strNum)
        retNum = intNum + 1
        strRetNum = str(retNum)
        retList = []
        for i in range(len(strRetNum)):
            retList.append(int(strRetNum[i]))
        return retList


t = Solution()
nums = [9, 9]
print(t.plusOne(nums))
