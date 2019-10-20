class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        ret = [1]  # start

        def get_triangle(last_line):
            current_line = [1]
            if len(last_line) == 1:
                return [1, 1]
            for num in range(len(last_line) - 1):
                current_line.append(last_line[num] + last_line[num + 1])
            current_line.append(1)
            return current_line

        for i in range(rowIndex):
            ret = get_triangle(ret)

        return ret
