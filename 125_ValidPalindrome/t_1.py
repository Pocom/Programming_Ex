class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for item in s:
            s = s.replace(item, '') if not item.isalnum() else s
        for i, item in enumerate(s[:(int(len(s)/2))]):
            if item != s[-i-1]:
                return False
        return True


t = Solution()
s0 = "race a car"
print(t.isPalindrome(s0))
