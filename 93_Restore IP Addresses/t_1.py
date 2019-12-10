class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def helper(tmp):
            if not tmp or (len(tmp) > 1 and tmp[0] == "0") or int(tmp) > 255:
                return False
            return True

        n, res = len(s), []

        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1, tmp2, tmp3, tmp4 = s[:i + 1], s[i + 1:j + 1], s[j + 1:k + 1], s[k + 1:]
                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)

        return res
