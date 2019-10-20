class Solution(object):
    def twoSum(self, nums, target):
        if not nums:  # if nums is None
            return None
        d = dict()

        for i, item in enumerate(nums):  # enumerate() -> (seq, element):tuple
            tmp = target - item  # item: n0, tmp: n1

            # method_1:
            # for key, value in d.items():
            #     if value == tmp:
            #         return [key, i]
            # d[i] = item

            # modified method:
            if tmp in d:
                return [d[tmp], i]
            d[item] = i
        return None


# testing
nums_t = [2, 7, 11, 15]
target_t = 9
t = Solution()
rList = t.twoSum(nums_t, target_t)
print(rList)
