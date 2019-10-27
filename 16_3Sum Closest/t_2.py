class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N, res = len(nums)-2, sum(nums[0:3])
        for n in range(N):
            left = n + 1
            right = N + 1
            while left < right:
                s = nums[n] + nums[left] + nums[right]
                if abs(target - res) > abs(s - target):
                    res = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return res
        return res