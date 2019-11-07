class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        res = str.split()
        return [*map(pattern.index, pattern)] == [*map(res.index, res)]


t = Solution()
pattern = "jquery"
str = "jquery"
t.wordPattern(pattern, str)
