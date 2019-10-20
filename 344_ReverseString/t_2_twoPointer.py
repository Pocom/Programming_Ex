class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n-1
        while left < (n//2):
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1; right -= 1