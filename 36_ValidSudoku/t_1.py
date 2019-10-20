class Solution:
    def isValidSudoku(self, board) -> bool:
        row_queue = [[],[],[],[],[],[],[],[],[]]
        col_queue = [[],[],[],[],[],[],[],[],[]]
        block_queue = [[],[],[],[],[],[],[],[],[]]
        for row, row_nums in enumerate(board):
            for col, num in enumerate(row_nums):
                if num != ".":
                    if row // 3 == 0: block = col // 3
                    elif row // 3 == 1: block = col//3+3
                    else: block = col//3+6
                    if num not in row_queue[row] and num not in col_queue[col] and num not in block_queue[block]:
                        row_queue[row].append(num)
                        col_queue[col].append(num)
                        block_queue[block].append(num)
                    else:
                        return False
        return True


t = Solution()
print(t.isValidSudoku())