class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        :param nums: List[int]
        :return: None
        """

        def bubble_sort(iterable):  # param: iterable is maybe a list object or a iterable object
            # 时间复杂度O(n^2) 可原地排序
            # 显然我们可以发现，排序完成的部分也会重复比较，所以在面向大量元素的排序时效率低下。
            # 所以一般可以采用较冒泡排序更优的插入排序。
            new_ls = list(iterable)
            ls_len = len(new_ls)

            # 一般思路，将最大的元素放在序列末尾，并排列数减一。
            while ls_len > 1:
                for i in range(ls_len - 1):
                    if new_ls[i] > new_ls[i + 1]:
                        new_ls[i], new_ls[i + 1] = new_ls[i + 1], new_ls[i]
                ls_len -= 1

            # 循环顺序与一般思路有所不同，是让每个位置上的元素与它后续元素循环比对，当当前位置的元素大于后续某个元素则交换。
            # 循环之后可以在每个位置上获得从该位置到末尾元素的最小元素，从而完成排序。
            # for i in range(ls_len):
            #     for j in range(i + 1, ls_len):
            #         if new_ls[i] > new_ls[j]:
            #             new_ls[i], new_ls[j] = new_ls[j], new_ls[i]

            return new_ls

        def insert_sort(iterable):
            new_ls = list(iterable)
            ls_len = len(new_ls)

            if ls_len in [1]: return new_ls

            # method 1
            for i in range(1, ls_len):
                for j in range(i, 0, -1):
                    if new_ls[j] < new_ls[j - 1]:
                        new_ls[j], new_ls[j - 1] = new_ls[j - 1], new_ls[j]
                    else:
                        break

            # method 2
            # There is a little difference between the two methods.
            # for i in range(1, ls_len):
            #     tmp = new_ls[i]
            #     j = i - 1
            #     while j >= 0 and tmp < new_ls[j]:
            #         new_ls[j + 1] = new_ls[j]
            #         j -= 1
            #     new_ls[j + 1] = tmp

            # method 3: 二分查找插入序列

            return new_ls

        def selection_sort(iterable):
            new_ls = list(iterable)
            ls_len = len(new_ls)
            for i in range(ls_len - 1):
                min_ind = i  # 保存最小值的索引
                for j in range(i + 1, ls_len):
                    if new_ls[min_ind] > new_ls[j]:
                        min_ind = j
                if i not in [min_ind]:
                    new_ls[i], new_ls[min_ind] = new_ls[min_ind], new_ls[i]
            return new_ls

        def quick_sort_1(iterable):  # 使用了Ω(n)的额外空间
            # O(nlogn)
            import random

            new_ls = list(iterable)
            ls_len = len(new_ls)

            if ls_len <= 1: return new_ls

            left, right, mid = [], [], []
            pivot = random.choice(new_ls)

            for num in new_ls:
                if num in [pivot]:
                    mid.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    right.append(num)

            return quick_sort_1(left) + mid + quick_sort_1(right)

        # 快速排序，原地排序方式。
        # 递归直到只有一个元素的情况。
        def quick_sort_2(iterable, first, last):  # in-place
            # O(nlogn)
            new_ls = list(iterable)
            if first >= last:
                return
            mid_value = new_ls[first]  # 取出第一个元素为基准值
            low = first
            high = last

            # 经过循环，low应该等于high，也就是
            while low < high:
                while low < high and new_ls[high] >= mid_value:
                    high -= 1
                new_ls[low] = new_ls[high]
                while low < high and new_ls[low] < mid_value:
                    low += 1
                new_ls[high] = new_ls[low]
            new_ls[low] = mid_value  # 将基准值放在中间

            quick_sort_2(new_ls, first, low - 1)
            quick_sort_2(new_ls, low + 1, last)

