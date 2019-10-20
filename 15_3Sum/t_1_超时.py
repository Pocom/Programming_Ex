class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        ret_list = []

        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-1):
                if j != i+1 and nums[j] == nums[j - 1]: continue
                for k in range(j+1, len(nums)):
                    if k != j + 1 and nums[k] == nums[k - 1]: continue
                    print(nums[i], nums[j], nums[k])
                    if not nums[i]+nums[j]+nums[k]:
                        print("enter")
                        ret_list.append([nums[i], nums[j], nums[k]])
        return ret_list


t = Solution()
print(t.threeSum([-1, 0, 1, 2, -1, -4]))
