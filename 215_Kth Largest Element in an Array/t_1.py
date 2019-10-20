class Solution:
    def findKthLargest(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        def quick_sort(ls, first, last):
            if first >= last: return
            mid_val = ls[first]
            low = first
            high = last
            while low < high:
                while low < high and ls[high]>=mid_val:
                    high -= 1
                ls[low] = ls[high]
                while low < high and ls[low]<mid_val:
                    low += 1
                ls[high] = ls[low]
            ls[low] = mid_val
            quick_sort(ls, first, low-1)
            quick_sort(ls, low+1, last)

        quick_sort(nums, 0, len(nums)-1)

        return nums[-k]

t = Solution()
nums = [3,2,1,5,6,4]

k = 2
t.findKthLargest(nums, k)