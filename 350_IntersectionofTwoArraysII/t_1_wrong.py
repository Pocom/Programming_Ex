class Solution:
    def intersect(self, nums1, nums2):
        ret = []
        if len(nums1) < len(nums2):
            for num1 in nums1:
                for num2 in nums2:
                    if num1 == num2:
                        ret.append(num1)
                        break
        else:
            for num2 in nums2:
                for num1 in nums1:
                    if num1 == num2:
                        ret.append(num2)
                        break
        return ret