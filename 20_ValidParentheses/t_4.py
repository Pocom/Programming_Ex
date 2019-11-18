class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}": "{", "]": "[", ")": "("}
        stack = []

        for item in s:
            if stack and item in dic and dic[item] in stack:
                stack.pop(-1)
            else:
                stack.append(item)

        return True if not stack else False
