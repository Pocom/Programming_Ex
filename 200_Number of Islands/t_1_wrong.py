class Solution:
    def numIslands(self, grid):
        """
        :param grid: List[List[str]]
        :return: int
        """
        if not grid: return 0
        cnt = 0
        if grid[0][0] == '1': cnt += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not r and c>0:  # 在第一行第二到最后一个
                    if grid[r][c-1] != '1' and grid[r][c] == '1':
                        if r+1<len(grid) and grid[r+1][c] != '1':
                            cnt += 1
                        elif r+1>=len(grid):
                            cnt += 1
                if not c and r>0:  # 在第一列第二个到最后一个
                    if grid[r-1][c] != '1' and grid[r][c] == '1':
                        if c+1<len(grid[0]) and grid[r][c+1] != '1':
                            cnt += 1
                        elif c+1>=len(grid[0]):
                            cnt += 1
                if r>0 and c>0:  # 除第一行第一列以外
                    if grid[r-1][c] != '1' and grid[r][c-1] != '1' and grid[r][c] == '1':
                        # 如果上面一个为0 左边也为0 且当前为1 则计数加一
                        cnt += 1
                    # 其他情况计数不变
        return cnt