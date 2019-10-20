class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            mark = 1
        elif x == 0:
            return 0
        else:
            mark = -1
            x -= 2 * x
        str_x = str(x)
        list_newX = [0] * len(str_x)
        j = len(str_x)
        for i in range(len(str_x)):
            list_newX[j - 1] = str_x[i]
            j -= 1
        list_newX = list(map(int, list_newX))
        str_newX = str(list_newX)
        str_newX = str_newX.strip('[]')
        str_newX = str_newX.replace(', ', '')
        return_x = int(str_newX)
        if return_x > (pow(2, 31) - 1) and mark == 1:
            return 0
        elif mark == -1 and return_x > pow(2, 31):
            return 0
        else:
            return mark * return_x


# testing
t = Solution()
print(t.reverse(12345))