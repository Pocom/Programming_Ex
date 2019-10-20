class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


# testing
t = Solution()
haystack = "aaaaa"
needle = "a"
print(t.strStr(haystack, needle))