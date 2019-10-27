class Solution:
    def fourSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[List[int]]
        """
        nums.sort()
        ans = set()
        L = len(nums)
        for i in range(L-2):
            for j in range(i+1, L-1):
                left = j + 1
                right = L - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    print(i,j,left,right)
                    print(nums[i], nums[j], nums[left], nums[right])
                    if s < target:
                        left += 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                    elif s > target:
                        right -= 1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                    else:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
        return list(map(list, ans))


t = Solution()
t.fourSum([1,0,-1,0,-2,2,1,0,-1,0,-2,2], 0)