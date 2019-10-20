class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]: zeros.append([i, j])
        for zero in zeros:
            matrix[zero[0]][:] = [0] * n
            for i in range(m):
                matrix[i][zero[1]] = 0
