class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1

        for key in dic.keys():
            if dic[key] == 1:
                return key
