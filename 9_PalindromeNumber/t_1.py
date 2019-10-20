"""

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            str_x = str(x)
            reversed_str_x = ''
            for i in range(len(str_x)-1, -1, -1):  # for .len() to 0
                reversed_str_x += str_x[i]
            if int(reversed_str_x) == x:
                return True
            else:
                return False


# testing
t = Solution()
print(t.isPalindrome(12321))
