class Solution:
    def letterCombinations(self, digits: str):
        # 循环个数不定 递归 BFS + hash_table
        phoneNum_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        list_str = []
        for digit in digits:
            list_str.append(phoneNum_dict[digit])
        for i in range(len(list_str)):
            for j in list_str[i]:
                return 0

