class Solution:
    def deleteAndEarn(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        # 不删除当前数字的时候，即是跳过前后数字，与198基本一致。
        if not nums: return 0
        ls = [0] + [0] * max(nums)
        for n in nums:
            ls[n] += n
        print(ls)
        last = now = 0
        for i in ls:
            last, now = now, max(last + i, now)
            print(last, now)
        print(now)
        return now


t = Solution()
t.deleteAndEarn([2])
