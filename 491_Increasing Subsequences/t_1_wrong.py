class Solution:
    def findSubsequences(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)

        l = r = 0
        arr, ret = [], []
        while r < len(nums):
            while r < len(nums)-1 and nums[r] <= nums[r + 1]:
                r += 1
            if l != r:
                if r == len(nums)-2 and nums[r] <= nums[r + 1]:
                    arr.append((nums[l:r + 2]))
                else:
                    arr.append(nums[l:r + 1])
            r += 1
            l = r
        print(arr)
        from itertools import combinations

        for nums in arr:
            for i in range(2, len(nums)):
                ret.extend(list(combinations(nums, i)))

        ret = [list(x) for x in list(dedupe(ret))]
        ret.extend(arr)
        print(ret)
        return ret

t = Solution()
t.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])