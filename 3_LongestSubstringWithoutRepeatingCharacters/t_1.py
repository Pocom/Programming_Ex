class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = list()
        ret_len = 0
        for str in s:
            if str_list.count(str) != 0:  # str exists in str_list
                print("列表中已有该元素: ", str)
                seq = str_list.index(str)
                ret_len = max(len(str_list), ret_len)
                str_list[:] = str_list[seq+1:]+[str]
            else:
                str_list.append(str)
            print("列表中有如下元素: ", str_list)
        ret_len = max(len(str_list), ret_len)
        return ret_len


t = Solution()
s = 'pwwkew'
longestSubstring = t.lengthOfLongestSubstring(s)
print(longestSubstring)
