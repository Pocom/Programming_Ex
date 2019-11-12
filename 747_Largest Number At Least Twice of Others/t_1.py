class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums) == 1: return 0

        max_n, last_max_n = (0, 0), (0, 0)

        for i, n in enumerate(nums):
            if max_n[1] < n:
                last_max_n, max_n = max_n, (i, n)
            elif last_max_n[1] < n:
                last_max_n = (i, n)

        print(last_max_n, max_n)
        if last_max_n[1] * 2 <= max_n[1]:
            return max_n[0]
        else:
            return -1


t = Solution()
t.dominantIndex([0, 0, 3, 2])
