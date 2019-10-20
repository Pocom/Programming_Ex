class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if s > sum(nums): return 0
        l = r = _sum = 0
        res = len(nums) + 1
        while r < len(nums):
            while _sum < s and r < len(nums):  # 右指针只在和大于目标时停止
                _sum += nums[r]
                r += 1
            while _sum >= s and l >= 0:
                res = min(res, r - l)
                _sum -= nums[l]
                l += 1
        return res

t = Solution()
s = 7
nums = [2,3,1,2,4,3]
print(t.minSubArrayLen(s, nums))
