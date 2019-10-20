class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if not nums[i] + nums[j] + nums[k]:
                        x = [nums[i], nums[j], nums[k]]
                        x.sort()
                        if x not in ret:
                            ret.append(x)
        return ret
