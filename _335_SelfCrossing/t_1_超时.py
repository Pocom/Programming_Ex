class Solution:
    def isSelfCrossing(self, x) -> bool:
        if not x: return False
        route = [[0, 0]]
        xi = yi = 0
        cnt = 0  # 每四个数字循环
        for movement in x:
            route_pos = []
            if cnt % 4 == 0:
                route_pos = list(map(lambda x: [xi, yi + x], range(1, movement + 1)))
            elif cnt % 4 == 1:
                route_pos = list(map(lambda x: [xi - x, yi], range(1, movement + 1)))
            elif cnt % 4 == 2:
                route_pos = list(map(lambda x: [xi, yi - x], range(1, movement + 1)))
            elif cnt % 4 == 3:
                route_pos = list(map(lambda x: [xi + x, yi], range(1, movement + 1)))
            for pos in route_pos:
                if pos in route:
                    return True
                else:
                    route.append(pos)
            cnt += 1
            xi, yi = route[-1][0], route[-1][1]
        return False


t = Solution()
print(t.isSelfCrossing([2, 1, 1, 2]))
