class Solution:
    def findSubsequences(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        if len(nums) <= 1: return []
        left, right, MAX = 0, 1, 1
        cur_stack = [nums[0]]
        ret = []
        arr = []
        while right < len(nums):
            if cur_stack[-1] <= nums[right]:
                MAX = 0
                cur_stack.append(nums[right])
                right += 1
            else:
                if len(cur_stack) == 1 and right < len(nums):
                    # cur_stack.pop(0)
                    # cur_stack.append(nums[right])
                    right += 1
                    continue
                if max(MAX, len(cur_stack)) > MAX:
                    MAX = max(MAX, len(cur_stack))
                    arr.append(list(cur_stack))

                if cur_stack: cur_stack.pop(-1)
                if not cur_stack:
                    left = right
                    right = left + 1
                    if right < len(nums):
                        cur_stack.append(nums[right])
            if right == len(nums) and len(cur_stack) >= 2:
                arr.append(list(cur_stack))
                if left < right:
                    left += 1
                    right = left + 1
                    cur_stack.clear()
                    cur_stack.append(nums[left])
            # if right == len(nums) and left < right - 1:
            #     left += 1
            #     cur_stack.clear()
            #     cur_stack.append(nums[left])
            #     right = left + 1
        print(arr)

        from itertools import combinations

        for nums in arr:
            for i in range(2, len(nums)):
                ret.extend(list(combinations(nums, i)))

        print(ret)
        def dedupe2(items, key=None):
            seen = set()
            for item in items:
                val = item if not key else key(item)
                if val not in seen:
                    yield item
                    seen.add(val)
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)

        ret = [list(x) for x in list(dedupe(ret))]
        ret.extend(arr)
        ret = [list(x) for x in list(dedupe2(ret, key=lambda x:tuple(x)))]
        print(ret)
        return ret

t = Solution()
t.findSubsequences([4,6,7,7])
