class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {"F": []}
        for n in nums:
            if n in dic["F"]:
                continue
            else:
                if n not in dic:
                    dic[n] = 1
                else:
                    del dic[n]
                    dic["F"].append(n)
        del dic["F"]
        return list(dic.keys())
