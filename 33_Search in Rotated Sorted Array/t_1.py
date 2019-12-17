from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        begin = nums[0]
        end = nums[-1]
        if target < begin and target > end:
            return -1

        flag = True if target >= begin else False

        if flag:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                elif nums[i] > target:
                    return -1
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == target:
                    return i
                elif nums[i] > end:
                    return -1

        return -1
