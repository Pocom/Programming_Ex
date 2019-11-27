from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(graph, N):
            stack = [graph[0]]
            visited = [0] + [1] * (N - 1)
            while stack:
                keys = stack.pop()
                if not keys: continue
                for k in keys:
                    if visited[k]:
                        stack.append(graph[k])
                        visited[k] = 0
            return visited

        return True if sum(dfs(rooms, len(rooms))) == 0 else False
