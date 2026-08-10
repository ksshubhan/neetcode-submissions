class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols
                or board[r][c] != "O" or (r, c) in visited):
                return
            
            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row >= 0 and col >= 0 and 
                row < rows and col < cols and
                board[row][col] == "O"):
                    dfs(row, col)

        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    dfs(r, c)
                if r == rows - 1:
                    dfs(r, c)
                if c == 0:
                    dfs(r, c)
                if c == cols - 1:
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
        
