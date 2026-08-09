class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visit = set()

        max_area = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols
                or (r, c) in visit or
                grid[r][c] == 0):
                return 0
            
            if (r, c) not in visit and grid[r][c] == 1:
                visit.add((r, c))
            
            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return area


        
        for r in range(rows):
            for c in range(cols):
                area = dfs(r, c)
                max_area = max(area, max_area)

        return max_area
