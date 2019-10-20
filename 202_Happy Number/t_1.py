class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n, cnt):

            if n == 1:
                return True
            if cnt > 30:
                return False
            str_n = str(n)
            next_n = sum([x ** 2 for x in list(map(int, str_n))])
            print(next_n)
            return helper(next_n, cnt + 1)

        return helper(n, 1)