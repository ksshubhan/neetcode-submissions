class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        subset = []

        def dfs(_open, _close):
            # base case - valid 
            if len(subset) == 2*n:
                res.append("".join(subset))
                return
            
            if _close > _open:
                return
            
            if _open < n:
                subset.append("(")
                dfs(_open + 1, _close)
                subset.pop()

            if _close < _open:
                subset.append(")")
                dfs(_open, _close + 1)
                subset.pop()

        dfs(0, 0)

        return res

