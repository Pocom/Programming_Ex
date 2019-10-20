class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]


t = Solution()
a = "11"; b = "1"
c = t.addBinary(a, b)
print(type(c))
print(c)