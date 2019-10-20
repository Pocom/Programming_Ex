class Solution:
    def searchInsert(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)


t = Solution()
print(t.searchInsert([1, 3, 5, 6], 5))
