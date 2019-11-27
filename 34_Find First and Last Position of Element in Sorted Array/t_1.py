class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                ret[0] = i
                j = i
                while j < len(nums) and nums[j] == target:
                    j += 1
                ret[1] = j - 1
                break

        return ret
