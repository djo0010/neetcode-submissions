class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        l = 0
        r = len(heights)-1
        while l < r:
            currMax = max(currMax, (r-l)*min(heights[l],heights[r]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return currMax