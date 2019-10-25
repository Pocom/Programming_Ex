class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[int]
        """
        if not matrix: return []

        m, n = len(matrix), len(matrix[0])
            
