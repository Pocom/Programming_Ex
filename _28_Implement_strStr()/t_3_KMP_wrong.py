class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  # wrong
        if not needle:
            return 0
        i = 0
        j = 0
        next_kmp = 0
        cnt = 0
        while i < haystack.__len__() and j < needle.__len__():
            print('haystack[{}] = {}'.format(i, haystack[i]))
            print('needle[{}] = {}'.format(j, needle[j]))
            print('next_kmp = ', next_kmp)
            print('needle[next_kmp] = {}'.format(needle[next_kmp]))

            if haystack[i] == needle[j]:
                print("相等")
                j += 1
                if j == 1:
                    cnt += 1
                print(j)
                if haystack[i] == needle[next_kmp] and j != 1:
                    next_kmp += 1
                    print('warning')
                else:
                    next_kmp = 0
            else:
                if haystack[i] == needle[next_kmp]:
                    next_kmp += 1
                cnt += 1
                j = 0
                if next_kmp != 0:
                    i = i - next_kmp
                    next_kmp = 0
            i += 1
            print('\t')
        if i >= haystack.__len__() and j < needle.__len__():
            return -1
        print('比较次数为：', cnt)
        print('字符串长度：', len(haystack))
        return i - len(needle)

# testing
t = Solution()
haystack = "aabaaabaaac"
needle = "aabaaac"




print(t.strStr(haystack, needle))
