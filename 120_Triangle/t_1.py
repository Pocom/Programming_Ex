class Solution:
    def minimumTotal(self, triangle):
        """
        :param triangle: List[List[int]]
        :return: int
        """
        if not triangle: return 0
        n = len(triangle)
        if n == 1: return triangle[0][0]
        queue = [triangle[0][0]]
        for i in range(1, n):
            next_queue = [queue[0]+triangle[i][0]]
            for j in range(1, i):
                next_queue.append(min((triangle[i][j]+queue[j-1]), triangle[i][j]+queue[j]))
            next_queue += [queue[-1]+triangle[i][-1]]
            queue = next_queue
            print(queue)
        return min(queue)


t = Solution()
t.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])