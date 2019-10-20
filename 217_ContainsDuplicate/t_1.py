class Solution:
    def containsDuplicate(self, nums) -> bool:
        num_dict = dict()
        for num in nums:
            if num in num_dict: return True
            else: num_dict.update({num: 1})
        return False