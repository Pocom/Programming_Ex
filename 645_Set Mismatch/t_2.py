class Solution:
    def findErrorNums(self, nums):
        """
        :param nums List[int]:
        :return: List[int]
        """
        err = sum(nums) - sum(set(nums))                # 找到重复出现的整数
        re = set(range(1, len(nums)+1)) - set(nums)     # 找到丢失的整数
        return [err, sum(re)]       # 将它们以数组形式返回
