class Solution:
    def groupAnagrams(self, strs):
        str_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in str_dict:
                str_dict[sorted_s] = [s]
            else:
                str_dict[sorted_s].append(s)
        return list(str_dict.values())