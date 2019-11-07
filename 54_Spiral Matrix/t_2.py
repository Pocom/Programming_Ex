class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 取首行，去除首行后，对矩阵翻转来创建新的矩阵，
        # 再递归直到新矩阵为[],退出并将取到的数据返回
        ret = []
        if not matrix:
            return ret
        ret.extend(matrix[0])  # 上侧
        new = [reversed(i) for i in matrix[1:]]
        print(matrix)
        if not new:
            return ret
        r = self.spiralOrder([i for i in zip(*new)])
        ret.extend(r)
        return ret


t = Solution()
input_ = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
t.spiralOrder(input_)
