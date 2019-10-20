class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret = ''
        if not s: return ret
        if len(s) >= 2 * k:
            for i in range(len(s) // (2 * k)):
                l = 2 * k * i
                m = 2 * k * i + k
                r = 2 * k * i + 2 * k
                ret += s[l:m][::-1] + s[m:r]
        rest_pos = len(s) // (2 * k) * 2 * k
        rest_num = len(s) - rest_pos
        if 2 * k > rest_num >= k:
            ret += s[rest_pos:rest_pos + k][::-1] + s[rest_pos + k:]
        elif k > rest_num > 0:
            ret += s[rest_pos:][::-1]
        return ret


t = Solution()
t.reverseStr("abcdfgsfsafzvree", 3)
