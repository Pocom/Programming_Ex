class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections, heapq
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
