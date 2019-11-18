class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = ret = 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                ret = max(ret, cnt)
                cnt = 0
        return max(ret, cnt)
