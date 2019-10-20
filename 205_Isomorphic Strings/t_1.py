class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s):
            if not s: return 0
            s_dict = {}
            s_nums = []
            cnt = 1
            for x in s:
                if x not in s_dict:
                    s_dict[x] = cnt
                    cnt += 1
                    s_nums.append(s_dict[x])
                else:
                    s_nums.append(s_dict[x])
            return int(''.join([str(t) for t in s_nums]))

        return helper(s) == helper(t)