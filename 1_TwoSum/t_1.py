"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1_TwoSum] = 2 + 7 = 9,
return [0, 1_TwoSum].

"""


class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return None
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i + 1:]:
                j = nums.index(diff, i + 1)
                return [i, j]
        return None


# testing
nums_t = [2, 2, 11, 15]
target_t = 26
t = Solution()
rList = t.twoSum(nums_t, target_t)
print(rList)
