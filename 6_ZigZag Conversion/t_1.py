class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        ls = [[] for _ in range(numRows)]
        i = 0
        down = True
        for x in s:
            ls[i].append(x)
            if down:
                i += 1
            else:
                i -= 1
            if i == numRows - 1:
                down = False
            elif i == 0:
                down = True
        print(ls)
        print(''.join(list(map("".join, ls))))
        return ''.join(list(map("".join, ls)))


t = Solution()
t.convert("PAYPALISHIRING", 3)