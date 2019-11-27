from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ret = []
        for row in A:
            ret.append(row[::-1])

        A = []
        for row in ret:
            tmp = []
            for x in row:
                tmp += [0] if x else [1]
            A.append(tmp)

        return A
