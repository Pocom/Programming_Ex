class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        [s.append(str) for str in s[::-1]]
        s[:] = s[n:]