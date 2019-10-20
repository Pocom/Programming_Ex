class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []

        ret = [[1]]  # start

        def get_triangle(last_line):
            current_line = [1]
            if len(last_line) == 1:
                return [1, 1]
            for num in range(len(last_line) - 1):
                current_line.append(last_line[num] + last_line[num + 1])
            current_line.append(1)
            return current_line

        for i in range(numRows - 1):
            get_tri = get_triangle(ret[i])
            ret.append(get_tri)

        return ret


t = Solution()
print(t.generate(4))