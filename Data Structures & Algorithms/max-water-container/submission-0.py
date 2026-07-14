class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        area = 0 
        max_area = 0 
        while i < j:
            min_height = min(heights[i], heights[j])
            area = (j - i) * min_height
            max_area = max(max_area, area)
            if min_height == heights[i]:
                i += 1
            elif min_height == heights[j]:
                j -= 1
        
        return max_area 