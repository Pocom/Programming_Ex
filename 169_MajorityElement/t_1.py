class Solution:
    def majorityElement(self, nums) -> int:
        dict = {}; n = len(nums)
        for num in nums:
            dict[num] = 1 if num not in dict else dict[num]+1
            if dict[num] > n//2: break
        sorted_nums = sorted(list(dict.items()), key=lambda x: x[1], reverse=True)
        return sorted_nums[0][0]


t = Solution()
res = t.majorityElement([1,1,1,1,3,3,3,3,2,2,2])
print(res)