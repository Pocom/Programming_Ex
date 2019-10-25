class Solution:
    def searchMatrix(self, matrix, target):
        """
        :param matrix: List[List[int]]
        :param target: int
        :return: bool
        """
        if not matrix or not matrix[0]: return False

        for x in matrix:
            print(x)

        if target < matrix[0][0] or target > matrix[-1][-1]: return False

        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) >> 1
            print(mid)
            r, c = mid // n, mid % n
            if matrix[r][c] > target:
                right = mid - 1
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                return True

        return False


t = Solution()
t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)