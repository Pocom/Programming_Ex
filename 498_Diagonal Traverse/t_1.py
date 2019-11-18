class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        i, j, m, n, ret, up = 0, 0, len(matrix), len(matrix[0]), [], True

        while i < m and j < n:
            ret.append(matrix[i][j])
            if up:
                if i == 0 or j == n - 1:
                    up = False
                    if j != n - 1:
                        j += 1
                    else:
                        i += 1
                else:
                    i -= 1;
                    j += 1
            else:
                if j == 0 or i == m - 1:
                    up = True
                    if i != m - 1:
                        i += 1
                    else:
                        j += 1
                else:
                    i += 1;
                    j -= 1

        return ret
