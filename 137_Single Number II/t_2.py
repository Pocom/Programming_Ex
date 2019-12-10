class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = None
        n = len(nums)
        for i in range(0, len(nums), 3):
            if i == n - 1 or nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]
