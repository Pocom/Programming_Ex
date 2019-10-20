class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return len(nums) and i+1  # 逻辑与 返回最后一个真值


t = Solution()
nums = [0, 0, 0, 0]
print(t.removeDuplicates(nums))
