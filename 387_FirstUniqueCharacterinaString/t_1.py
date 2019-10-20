class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        s_dict = {}
        for pos, item in enumerate(s):
            if item not in s_dict:
                s_dict.update({item: pos})
            else:
                s_dict[item] = -1
        for key, value in s_dict.items():
            if value != -1:
                return value
        return -1