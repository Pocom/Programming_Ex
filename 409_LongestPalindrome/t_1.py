class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s: return 0
        ret = odd = 0
        s_dict = {x: 0 for x in set(sorted(s))}
        for s_str in s:
            if s_str in s_dict:
                s_dict[s_str] += 1
        print(s_dict)
        for val in s_dict.values():
            if not val % 2:
                ret += val
            else:
                ret += val - 1
                odd = 1
        return ret + odd

t = Solution()
print(t.longestPalindrome("abccccdd"))
