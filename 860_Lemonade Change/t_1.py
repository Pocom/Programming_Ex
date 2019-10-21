class Solution:
    def lemonadeChange(self, bills):
        """
        :param bills: List[int]
        :return: bool
        """
        check_5 = 0
        check_10 = 0
        for b in bills:
            if b == 5:
                check_5 += 1
            elif b == 10:
                if check_5 > 0:
                    check_5 -= 1
                else:
                    return False
                check_10 += 1
            elif b == 20:
                if check_10 > 0 and check_5 > 0:
                    check_10 -= 1
                    check_5 -= 1
                elif check_10 <= 0 < check_5:
                    check_5 -= 3
                    if check_5 < 0:
                        return False
                else:
                    return False
        return True


t = Solution()
t.lemonadeChange([10,10])