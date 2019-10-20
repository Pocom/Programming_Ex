class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i] = 0
                nums[cnt] = num
                cnt += 1


t = Solution()
nums_list = [0, 1, 1, 2, 3,0,5]
t.moveZeroes(nums_list)
print(nums_list)