class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        _set = set()

        for i in range(len(nums)):
            if nums[i] in _set:
                return True
            _set.add(nums[i])
            if len(_set) > k:
                _set.remove(nums[i - k])

        return False
