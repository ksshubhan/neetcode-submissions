class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visit = set()

        queue = []

        time, fresh = 0, 0

        def bfs(r, c):
            if (r < 0 or c < 0 or r == rows or 
                c == cols or (r, c) in visit
                or grid[r][c] != 1):
                return
            
            visit.add((r, c))
            queue.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:

            for i in range(len(queue)):
                r, c = queue.pop(0)
                 
                grid[r][c] = 2

                old_length = len(queue)
                
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

                fresh = fresh - (len(queue) - old_length)

            time += 1
        
        if fresh == 0:
            return time

        return -1     