class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        size = len(points)
        if size < 2:
            return size

        # 按照区间的末尾端点排序
        points.sort(key=lambda x: x[1])
        res = 1

        # 最远距离：使用当前这只箭能引爆气球的最远距离
        end = points[0][1]

        for i in range(1, size):
            if points[i][0] > end:
                end = points[i][1]
                res += 1
        return res
