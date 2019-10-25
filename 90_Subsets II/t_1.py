class Solution:
    def subsetsWithDup(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        if not nums: return [[]]
        nums.sort()
        res = [[nums[0]]]
        last_num, last_res = nums[0], [[nums[0]]]
        for num in nums[1:]:
            if last_num == num:
                last_res = [x + [num] for x in last_res]
            else:
                last_res = [x + [num] for x in res] + [[num]]
            last_num = num
            res += last_res
        res += [[]]
        print(res)
        return res


t = Solution()
t.subsetsWithDup([1,2,2,4])