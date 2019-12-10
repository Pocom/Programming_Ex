from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        N = len(gas)

        def helper(pos, reserve):
            for _ in range(N):
                if reserve - cost[pos] < 0:
                    return False
                reserve -= cost[pos]
                pos = 0 if pos + 1 == N else pos + 1
                reserve += gas[pos]
            return True

        for i in range(N):
            if helper(i, gas[i]):
                return i

        return -1
