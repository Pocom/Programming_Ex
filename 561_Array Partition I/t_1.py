class Solution:
    def arrayPairSum(self, nums):
        """
        :param nums: List[int]
        :return: int
        """

        def quick_sort(new_ls, first, last):  # in-place
            # O(nlogn)
            # new_ls = list(iterable)
            if first >= last: return

            mid_value = new_ls[first]  # 取出第一个元素为基准值
            low = first
            high = last

            while low < high:
                while low < high and new_ls[high] >= mid_value:
                    high -= 1
                new_ls[low] = new_ls[high]
                while low < high and new_ls[low] < mid_value:
                    low += 1
                new_ls[high] = new_ls[low]
            new_ls[low] = mid_value  # 将基准值放在中间

            quick_sort(new_ls, first, low - 1)
            quick_sort(new_ls, low + 1, last)

        quick_sort(nums, 0, len(nums) - 1)

        return sum(nums[::2])


t = Solution()
t.arrayPairSum([1, 2, 3, 2, 5, 6, 8, 1])
