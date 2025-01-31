class NumArray:

    def __init__(self, nums):
        """
        :param nums: List[int]
        """
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        # if i == j:
        #     return self.nums[-1] if j == len(self.nums) - 1 else self.nums[i]
        # else:
        #     return sum(self.nums[i:j+1]) if j < len(self.nums) - 1 else sum(self.nums[i:])
        return sum(self.nums[i:j + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
