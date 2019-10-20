class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2: return min(height[0], height[1])
        l = 0
        r = len(height) - 1
        area_max = 0
        while l < r:
            area_max = max(area_max, min(height[l], height[r])*(r-l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area_max