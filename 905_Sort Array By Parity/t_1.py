class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []

        for n in A:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)

        return even + odd
