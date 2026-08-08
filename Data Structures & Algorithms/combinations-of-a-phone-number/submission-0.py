class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        subset = []
        
        hash_map = {2: ["a", "b", "c"], 
                    3: ["d", "e", "f"], 
                    4: ["g", "h", "i"], 
                    5: ["j", "k", "l"], 
                    6: ["m", "n", "o"], 
                    7: ["p", "q", "r", "s"], 
                    8: ["t", "u", "v"], 
                    9: ["w", "x", "y", "z"]}
        
        def dfs(i):
            if len(subset) == len(digits):
                res.append("".join(subset))
                return
            
            key = digits[i]
            for j in hash_map[int(key)]:
                subset.append(j)
                dfs(i + 1)
                subset.pop()

            
        dfs(0)

        if res == [""]:
            res = []
        return res
            
