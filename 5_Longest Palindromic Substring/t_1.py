class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        l, r, res, MAX, ret = 0, 1, 0, 0, ''

        def helper(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        while r < len(s):
            res = max(res, helper(s, l, r))
            if res > MAX:
                MAX, ret = res, s[l - (res // 2 - 1):r + (res // 2 - 1) + 1]
            r += 1
            res = max(res, helper(s, l, r))
            if res > MAX:
                MAX, ret = res, s[l - (res // 2 - 1):r + (res // 2 - 1) + 1]
            l += 1

        return ret