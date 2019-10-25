class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """
        if not nums1 or not nums2:
            nums1[:] = nums1 + nums2
            return nums1[len(nums1)//2] if len(nums1)//2 == (len(nums1)-1)//2 else float(nums1[(len(nums1)-1)//2] + nums1[len(nums1)//2]) / 2

        len_1 = len(nums1)
        len_2 = len(nums2)
        len_3 = len_1 + len_2
        i, j = 0, 0
        nums = []
        while i < len_1 and j < len_2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        print(nums)
        if i < len_1:
            nums.extend(nums1[i:])
        elif j < len_2:
            nums.extend(nums2[j:])
        print(nums)
        return nums[len_3 // 2] if len_3 // 2 == (len_3 - 1) // 2 else float(
            nums[(len_3 - 1) // 2] + nums[len_3 // 2]) / 2


t = Solution()
t.findMedianSortedArrays([1,3], [2])