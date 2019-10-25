class Solution:
    def subsets(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        if not nums: return [[]]
        ret = []
        for num in nums:
            ret += [x + [num] for x in ret] + [[num]]
        ret += [[]]
        return ret

t = Solution()
t.subsets([1,2,3,4])