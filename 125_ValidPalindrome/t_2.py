class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        将python的简洁发挥到了极致
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
