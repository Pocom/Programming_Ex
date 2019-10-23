class Solution:
    def searchInsert(self, nums, target):
        _len = len(nums)
        if target > nums[-1]:
            return _len
        left, right = 0, _len - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
