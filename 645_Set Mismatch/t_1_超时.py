class Solution:
    def findErrorNums(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        # nums 无序
        # 找到其中重复的和缺失的数字
        _len = len(nums)
        res = []
        for i in range(1, _len+1):
            if i in nums:
                nums.pop(nums.index(i))
            else:
                res.append(i)
        res.insert(0, nums[0])
        return res
