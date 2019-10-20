"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

"""


class Solution:  # wrong, "{()}"should be right, but
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for item in s:
            stack.append(ord(item))  # ASCⅡ -> UNICODE
            if stack.__len__() == 2:
                if stack[0] + 1 != stack[1] and stack[0] + 2 != stack[1]:
                    return False
                stack.clear()
        if stack.__len__() == 1:
            return False
        return True


t = Solution()
print(t.isValid("(){}["))