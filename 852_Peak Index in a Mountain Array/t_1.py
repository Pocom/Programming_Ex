class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A) - 1):
            if i + 1 > len(A) - 1: break
            if A[i - 1] < A[i] > A[i + 1]:
                return i
