class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :param numCourses: int
        :param prerequisites: List[List[int]]
        :return: bool
        """

        len_c = len(prerequisites)
        if not len_c: return True

        in_deg = [0 for _ in range(numCourses)]  # 入度表
        adj = [set() for _ in range(numCourses)]  # 邻接表

        for cou, pre in prerequisites:
            in_deg[cou] += 1
            adj[pre].add(cou)

        queue = []
        for i in range(numCourses):
            if not in_deg[i]:  # 如果某个课程的入度为 0 ，意味着它很有可能是基础课
                queue.append(i)

        cnt = 0
        while queue:
            top = queue.pop(0)  # 取出其中的基础课
            cnt += 1
            for successor in adj[top]:  # 取出基础课的邻接元素
                in_deg[successor] -= 1  # 使其入度 - 1
                if not in_deg[successor]:  # 如果减至0 则加入基础课队列
                    queue.append(successor)

        return cnt == numCourses
