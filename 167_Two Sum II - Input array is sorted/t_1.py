class Solution:
    def twoSum(self, numbers, target):
        """
        :param numbers: List[int]
        :param target: int
        :return: List[int]
        """
        if not numbers: return None
        i, j = 0, len(numbers)-1
        while i<j:
            s = numbers[i]+numbers[j]
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [i+1, j+1]
        return None
