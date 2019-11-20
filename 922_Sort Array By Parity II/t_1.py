class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        tmp_odd = [[], []]
        tmp_even = [[], []]
        for i, item in enumerate(A):
            if (i % 2 == 0 and item % 2 == 0) or (i % 2 != 0 and item % 2 != 0):
                continue
            elif i % 2 == 0 and item % 2 != 0:  # 偶数位 插偶数
                tmp_even[0].append(i)
                tmp_odd[1].append(item)
                if tmp_even[1]:
                    A[i] = tmp_even[1].pop()
                    tmp_even[0].pop()
            elif i % 2 != 0 and item % 2 == 0:  # 奇数位 插奇数
                tmp_odd[0].append(i)
                tmp_even[1].append(item)
                if tmp_odd[1]:
                    A[i] = tmp_odd[1].pop()
                    tmp_odd[0].pop()

        if tmp_even[0]:
            for i, j in zip(tmp_even[0], tmp_even[1]):
                A[i] = j
        if tmp_odd[0]:
            for i, j in zip(tmp_odd[0], tmp_odd[1]):
                A[i] = j

        return A
