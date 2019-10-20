class Solution:
    def singleNumber(self, nums) -> int:
        numDict = dict()
        for num in nums:
            if num in numDict: numDict[num] = -1
            else: numDict.update({num: 1})
        for key, val in numDict.items():
            if val == 1: return key


t = Solution()
print(t.singleNumber([1, 1, 2]))
