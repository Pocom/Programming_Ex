class Solution:
    def topKFrequent(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: List[int]
        """
        dict_num, ls, res = {}, [], []

        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                dict_num[num] += 1
        print(dict_num)
        for num, freq in dict_num.items():
            ls.append((num, freq))
        print(ls)
        ls[:] = sorted(ls, key=lambda x: x[1])
        print(ls)
        for tup in ls[::-1]:
            res.append(tup[0])
            if len(res) == k: break
        return res


t = Solution()
nums = [1,1,1,2,2,3]


k = 2
print(t.topKFrequent(nums, k))