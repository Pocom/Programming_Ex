class Solution:
    def search(self, grid, row, col):
        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == '0':
            return
        else:
            grid[row][col] = '0'
            self.search(grid, row + 1, col)
            self.search(grid, row, col + 1)
            self.search(grid, row - 1, col)
            self.search(grid, row, col - 1)

    def numIslands(self, grid) -> int:
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    cnt += 1
                    self.search(grid, r, c)
        return cnt