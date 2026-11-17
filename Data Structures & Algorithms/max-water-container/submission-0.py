class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        vol = min(heights[i], heights[j])*(j-i)
        while i < j:
            if heights[i] > heights[j]:
                j -= 1
                vol = max(vol, (min(heights[i], heights[j])*(j-i)))
            else:
                i += 1
                vol = max(vol, (min(heights[i], heights[j])*(j-i)))
        return vol