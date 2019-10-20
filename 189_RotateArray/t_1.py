class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for num in nums[::-1]:
            if k == 0: break
            nums.insert(0, num)
            nums.pop(-1)
            k -= 1