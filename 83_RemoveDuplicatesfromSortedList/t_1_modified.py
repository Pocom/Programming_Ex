class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2:
            if m == 0:
                nums1[:m+n] = nums2[:]
            else:
                ret_arr = [0] * (m+n)
                i = j = k = 0
                while k < m+n:
                    if nums1[i] > nums2[j]: ret_arr[k] = nums2[j]; j += 1
                    else: ret_arr[k] = nums1[i]; i += 1
                    if i == m: ret_arr[i+j:] = nums2[j:]; break
                    elif j == n: ret_arr[i+j:] = nums1[i:m]; break
                    k += 1
                nums1[:m+n] = ret_arr[:]


t = Solution()
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

t.merge(nums1, m, nums2, n)
print(nums1)