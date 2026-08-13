class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(index):
            if index in memo:
                return memo[index]

            if index == len(s):
                return True
            
            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordDict:
                    if helper(i) == True:
                        memo[index] = True
                        return True 
                    

            memo[index] = False 
            return False 
        
        return helper(0)