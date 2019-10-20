class Solution:
    def __init__(self):
        self.ret = [[1]]
        self.line = []

    def get_num(self, i, j):
        if j == 0 or i == j:
            return 1
        return self.ret[i - 1][j - 1] + self.ret[i - 1][j]

    def generate(self, numRows: int):
        if not numRows: return []

        for row in range(1, numRows):
            for col in range(row+1):
                self.line.append(self.get_num(row, col))
            self.ret.append(self.line)
            self.line = []

        return self.ret


t = Solution()
t.generate(2)