class Solution:
    def intersection(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: List[int]
        """
        return list(set(nums1) & set(nums2))
