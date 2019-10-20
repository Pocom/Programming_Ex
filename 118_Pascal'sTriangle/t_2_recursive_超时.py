class Solution:
    def generate(self, numRows: int):
        if not numRows: return []

        def get_number(row: int, col: int):
            if col == 1 or row == col:
                return 1
            return get_number(row-1, col-1) + get_number(row-1, col)

        ret = []
        for numRow in range(1, numRows+1):
            ret_row = []
            for numCol in range(1, numRow+1):
                ret_row.append(get_number(numRow, numCol))
            ret.append(ret_row)
        return ret


t = Solution()
print(t.generate(3))