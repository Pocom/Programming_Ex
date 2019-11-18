class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: int(x / y)}
        for item in tokens:
            if item in op:
                y = stack.pop()
                x = stack.pop()
                stack.append(op[item](x, y))
            else:
                stack.append(int(item))
        return stack[-1]
