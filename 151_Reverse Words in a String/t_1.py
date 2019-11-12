class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])
        return " ".join(list(filter(lambda x: x, s.strip().split(" ")[::-1])))


t = Solution()
print(t.reverseWords("a good   example"))
