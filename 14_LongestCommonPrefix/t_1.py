"""

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        numsOfList = len(strs)
        prefix = []
        min_len = min(map(len, strs))
        print(min_len)
        prefix.extend(strs[0])
        prefix = prefix[:min_len]
        for i in range(1, numsOfList):
            if not prefix:
                return ''.join(prefix)
            for seq, item in enumerate(strs[i]):
                if prefix[seq] != item:
                    prefix = [] if seq == 0 else prefix[:seq]
                    break
                if seq == min_len - 1:
                    break
            min_len = len(prefix)
        return ''.join(prefix)


t = Solution()
print(t.longestCommonPrefix(["flower", "flow", "flight"]))
print(t.longestCommonPrefix([]))
print(t.longestCommonPrefix(["dog", "racecar", "car"]))