class Solution:  # wrong, "{()}"should be right, but
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        back_str = {')', ']', '}'}
        stack = list()
        stack.append(ord(s[0]))  # ASCⅡ -> UNICODE
        for item in s[1:]:
            stack.append(ord(item))
            if item in back_str and len(stack) > 1:
                if stack[-2] + 1 != stack[-1] and stack[-2] + 2 != stack[-1]:
                    return False
                stack.pop(-1); stack.pop(-1)
        if stack:
            return False
        return True


t = Solution()
print(t.isValid("{})"))