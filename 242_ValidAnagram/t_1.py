class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        for str in t:
            if str not in s_list:
                return False
            else:
                s_list.pop(s_list.index(str))
        return True


t = Solution()
s1 = "anagram"
s2 = "nagaram"
print(t.isAnagram(s1, s2))