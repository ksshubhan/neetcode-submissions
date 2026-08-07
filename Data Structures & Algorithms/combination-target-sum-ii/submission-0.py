class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, total):
            # base case 1 - valid
            if target == total:
                res.append(subset.copy())
                return
            
            # base case 2 - invalid 
            if i >= len(candidates) or total > target:
                return
            
    
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)
        
        dfs(0, 0)

        return res