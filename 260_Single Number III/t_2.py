class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                del dic[n]
        return list(dic.keys())
