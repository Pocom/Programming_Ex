class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        ret = []

        for n in A:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)

        for o, e in zip(odd, even):
            ret.extend([e, o])

        return ret
