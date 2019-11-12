class Solution:
    def frequencySort(self, s: str) -> str:
        if not s: return ""

        dic = {}

        for alpha in s:
            if alpha not in dic:
                dic.setdefault(alpha, 1)
            else:
                dic[alpha] += 1

        ret = ""

        for key in sorted(dic, key=dic.__getitem__, reverse=True):
            for _ in range(dic[key]):
                ret += key

        return ret


t = Solution()
print(t.frequencySort("Aabb"))
