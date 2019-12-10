from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        in_deg = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]

        for cur, pre in prerequisites:
            in_deg[cur] += 1
            adj[pre].add(cur)

        queue = []
        for i in range(numCourses):
            if not in_deg[i]:
                queue.append(i)

        ret = []
        while queue:
            cur = queue.pop(0)
            ret.append(cur)
            for nxt in adj[cur]:
                in_deg[nxt] -= 1
                if not in_deg[nxt]:
                    queue.append(nxt)

        return ret if numCourses == len(ret) else []
