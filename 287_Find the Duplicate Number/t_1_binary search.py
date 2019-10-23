class Solution:
    def findDuplicate(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        # nums involve n+1 integers (1 - n)
        _len = len(nums)
        left, right = 1, _len-1  # 1 - n
        while left < right:
            cnt = 0  # 计算小于中位数的个数
            mid = (left + right) >> 1  # 中位数 偶数情况下，则是偏左的一个
            for num in nums:
                if num <= mid:  # 如果数字小于中位数
                    cnt += 1  # 计数加一
            if cnt > mid:  # 如果统计值大于中位数，则表示重复数字在中位数左侧的数字里出现，所以right = mid，因为上面是num <= mid，所以此时不能排除mid
                right = mid
            else:  # 如果统计值小于中位数，则表示重复数字在中位数右侧的数字里，同时中位数不可能是重复数字，所以left = mid + 1
                left = mid + 1
        return left
