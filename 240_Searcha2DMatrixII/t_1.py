class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        if matrix[0][0] > target or matrix[m-1][n-1] <target: return False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False


t = Solution()
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
target = 5
print(t.searchMatrix(matrix, target))
