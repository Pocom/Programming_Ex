"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            mark = ''
        elif x == 0:
            return 0
        else:
            mark = '-'
            if x < -(pow(2, 31) - 1) :
                return 0
            else:
                x -= 2 * x
        str_X = str(x)
        list_newX = [0] * len(str_X)
        j = len(str_X)
        for i in range(len(str_X)):
            list_newX[j - 1] = str_X[i]
            j -= 1
        list_newX = list(map(int, list_newX))
        str_newX = str(list_newX)
        str_newX = str_newX.strip('[]')
        str_newX = str_newX.replace(', ', '')
        return int(mark+str_newX)