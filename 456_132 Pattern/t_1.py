class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        stack = []
        _min = - sys.maxsize

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < _min:
                return True
            while stack and nums[i] > stack[-1]:
                _min = stack.pop()
            stack.append(nums[i])
            print("stack: {}, min: {}".format(stack, _min))
        return False


t = Solution()
t.find132pattern([1, 2, 3, 2, 5, 6, 8, 1])
