class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


# testing
t = Solution()
haystack = "aaaaa"
needle = "bba"
print(t.strStr(haystack, needle))
