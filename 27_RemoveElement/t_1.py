class Solution:
    def removeElement(self, nums, val):
        """
        :param nums: List[int]
        :param val: int
        :return: int
        """
        cnt_val = nums.count(val)
        for i in range(cnt_val):
            nums.remove(val)
        return nums.__len__()


# testing
t = Solution()
nums = [0,1,2,2,3,0,4,2]
len = t.removeElement(nums, 2)
print(len)
print(nums)