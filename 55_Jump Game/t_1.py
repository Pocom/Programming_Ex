class Solution:
    def canJump(self, nums):
        cur = 0
        mmax = 0
        while cur <= mmax:  # 当前位置小于最大达到位置
            mmax = max(cur + nums[cur], mmax)
            cur += 1

            if mmax >= len(nums) - 1:  # 起始是从0开始 故减1
                return True

        return False
