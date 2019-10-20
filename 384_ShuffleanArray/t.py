# 测试为什么在函数里面还要继续使用list(self.original)


import random


class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        print("1: ", self.original)
        print(type(self.original))
        self.original = list(self.original)  # 何用？
        print("2: ", self.original)
        print(type(self.original))

        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array


# Your Solution object will be instantiated and called as such:
nums1 = [1, 2, 3]
obj = Solution(nums1)
param_1 = obj.reset()
param_2 = obj.shuffle()
