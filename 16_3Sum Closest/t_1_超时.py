class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        from sys import maxsize
        length = len(nums)
        ls = []
        SUM = res = 0
        diff = maxsize
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    SUM = nums[i] + nums[j] + nums[k]
                    if diff > abs(SUM - target):
                        diff = abs(SUM - target)
                        res = SUM
        return res
