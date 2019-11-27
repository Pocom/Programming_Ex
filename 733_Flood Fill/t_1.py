from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        oldColor, image[sr][sc] = image[sr][sc], newColor
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]

        def bfs(matrix, m, n, stack, old, new):
            if not stack: return
            direction, _next = [(1, 0), (-1, 0), (0, 1), (0, -1)], []

            while stack:
                center = stack.pop()
                oldR, oldC = center[0], center[1]
                for i, j in direction:
                    newR, newC = oldR + i, oldC + j
                    if 0 <= newR <= m - 1 and 0 <= newC <= n - 1 and matrix[newR][newC] == old:
                        _next.append((newR, newC))
                        matrix[newR][newC] = new
                stack = _next
                print(stack)

        # def modified_bfs(matrix, m, n, stack, val):
        #     direction, _next = [(1, 0), (-1, 0), (0, 1), (0, -1)], []
        #
        #     visited = []
        #
        #     while stack:
        #         center = stack.pop()
        #         oldR, oldC = center[0], center[1]
        #         for i, j in direction:
        #             newR, newC = oldR + i, oldC + j
        #             if 0 <= newR <= m - 1 and 0 <= newC <= n - 1 and matrix[newR][newC] == val and (newR, newC) not in visited:
        #                 _next.append((newR, newC))
        #                 visited.append((newR, newC))
        #         stack = _next

        if oldColor != newColor:
            bfs(image, m, n, stack, oldColor, newColor)
        # else:
        #     modified_bfs(image, m, n, stack, oldColor)
        return image


t = Solution()
print(t.floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1))
