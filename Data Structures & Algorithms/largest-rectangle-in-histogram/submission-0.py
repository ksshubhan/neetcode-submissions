class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        area = 0

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(area, max_area)
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            area =  h * (len(heights) - i)
            max_area = max(area, max_area)

        return max_area
