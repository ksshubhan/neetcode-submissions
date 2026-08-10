class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visit):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visit):
                return
            
            if (r, c) not in visit:
                visit.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc 

                if (row >= 0 and col >= 0 and 
                    row < rows and col < cols and 
                    heights[row][col] >= heights[r][c] and 
                    (row, col) not in visit):
                    dfs(row, col, visit)
        
        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    dfs(r, c, pacific)
                if c == 0:
                    dfs(r, c, pacific)


        for r in range(rows):
            for c in range(cols):
                if r == rows - 1:
                    dfs(r, c, atlantic)
                if c == cols - 1:
                    dfs(r, c, atlantic)
        
        visited = atlantic & pacific
        res = []
        for t in visited:
            res.append(list(t))
        
        return res
            