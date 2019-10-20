from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = [[nums[0]]]
        idx_map = {nums[0]: -1}
        for i in range(1, len(nums)):
            if nums[i] not in idx_map:
                print(res)
                idx_map[nums[i]] = len(res)
                print(idx_map[nums[i]])
                res += [lst + [nums[i]] for lst in res if lst[-1] <= nums[i]] + [[nums[i]]]
                print("number not in map, current number: ", nums[i], ', current result: ', res)
            else:
                tmp = len(res)
                res += [res[j] + [nums[i]] for j in range(tmp) if res[j][-1] <= nums[i] and j >= idx_map[nums[i]]]
                idx_map[nums[i]] = tmp
        return [lst for lst in res if len(lst) > 1]


t = Solution()
t.findSubsequences([1,2,3,1,2,3, 2, 2])