class Solution:
    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[int]
        """
        if not matrix: return []

        u, d, l, r, ans = 0, len(matrix) - 1, 0, len(matrix[0]) - 1, []

        while True:
            for i in range(l, r + 1):  # from left to right
                ans.append(matrix[u][i])

            u += 1
            if u > d: break
            for i in range(u, d + 1):  # from up to down
                ans.append(matrix[i][r])

            r -= 1
            if r < l: break
            for i in range(r, l - 1, -1):  # from right to left
                ans.append(matrix[d][i])

            d -= 1
            if d < u: break
            for i in range(d, u - 1, -1):  # from down to up
                ans.append(matrix[i][l])

            l += 1
            if l > r: break

        return ans


t = Solution()
input_ = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(t.spiralOrder(input_))
