class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        res = [False]

        subset = []

        visit = set()

        def dfs(i, r, c):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r == rows or 
                c == cols or (r, c) in visit 
                or board[r][c] != word[i]):
                return False
            
            visit.add((r, c))

            if board[r][c] == word[i]:
                i += 1
            
            res = (
                dfs(i, r - 1, c) or
                dfs(i, r + 1, c) or
                dfs(i, r, c - 1) or
                dfs(i, r, c + 1) 
            )
            visit.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        
        return False