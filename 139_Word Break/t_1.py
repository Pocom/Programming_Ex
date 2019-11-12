class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        breakp = [0] * (len(s) + 1)

        for i in range(len(s) + 1):
            print("i", i)
            for j in breakp[:i]:
                print("s[{}:{}]".format(j, i), s[j:i])
                if s[j:i] in wordDict:
                    breakp[i] = i
                    break

        return breakp[-1] == len(s)


t = Solution()
t.wordBreak("aaaaaaa", ["aaaa", "aaa"])
