class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A: return []

        ret, stack, j = [], [], 0
        for num in A:
            if num < 0:
                stack.append(- num)
            elif num == 0:
                A[j] = 0;
                j += 1
            else:
                while stack:
                    if num < stack[-1]:
                        A[j] = num;
                        j += 1;
                        break
                    else:
                        A[j] = stack.pop();
                        j += 1

        while stack:
            A[j] = stack.pop();
            j += 1

        for num in A:
            ret.append(num ** 2)

        return ret
