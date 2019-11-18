class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            min_n = nums[0]
            for n in nums[::-1]:
                if min_n > n:
                    min_n = n
                else:
                    return min_n
