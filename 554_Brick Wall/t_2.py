class Solution:
    def leastBricks(self, wall):
        dic = {0: 0}
        for l in wall:
            s = 0
            if len(l) in [1]: continue
            for v in l[:-1]:
                s += v
                dic[s] = dic.get(s, 0) + 1
        return len(wall) - max(dic.values())


t = Solution()
print(t.leastBricks([[10000], [10000], [10000]]))
