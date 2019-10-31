class Solution:
    def leastBricks(self, wall):
        """
        :param wall: List[List[int]]
        :return: int
        """
        line = [0] * sum(wall[0])
        # print(line)
        for row in wall:
            start = end = 0
            # print("next row")
            for brick in row:
                end += brick
                # print(start, end)
                line[start:end] = [n + 1 for n in line[start:end]]
                start = end + 1
            # print(line)
        # print(line)
        return min(line)


t = Solution()
t.leastBricks([[100000000], [100000000], [100000000]])
