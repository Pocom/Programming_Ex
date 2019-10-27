class Solution:
    def permute(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        if not nums: return []

        queue = [[nums[0]]]
        if len(nums) in [1]: return queue

        for i, n in enumerate(nums[1:]):
            next_queue = []
            for j in range(len(queue)):
                pos = 0
                tmp = []
                while pos < i+2:
                    tmp[:] = queue[j]
                    tmp.insert(pos, n)
                    next_queue += [tmp[:]]
                    pos += 1
            queue = next_queue
        return queue

t = Solution()
t.permute([1,2,3])