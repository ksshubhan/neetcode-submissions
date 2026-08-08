class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()

        PosDiag = set()

        negDiag = set()

        grid = []
        count = 1
        for i in range(n):
            row = []
            for j in range(n):
                row.append(".")
                count += 1
            grid.append(row)
        
        def dfs(r):
            if r == n:
                grid_s = []
                for row in grid:
                    grid_s.append("".join(row))
                
                res.append(grid_s)
                return

            for c in range(len(grid[r])):
                if c not in cols:
                    if r + c not in PosDiag:
                        if r - c not in negDiag:
                                grid[r][c] = "Q"
                                cols.add(c)
                                PosDiag.add(r + c)
                                negDiag.add(r - c)
                                dfs(r + 1)
                                grid[r][c] = "."
                                cols.remove(c)
                                PosDiag.remove(r + c)
                                negDiag.remove(r - c)

        dfs(0)

        return res