class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(remain):
            if remain in memo:
                return memo[remain]

            if remain < 0:
                return -1

            if remain == 0:
                return 0
        
            min_c = amount + 1 
            for i in range(len(coins)):
                res = helper(remain - coins[i])
                if res == -1:
                    continue
                else:
                    c = 1 + res
                    if c < min_c:
                        min_c = c
            
            memo[remain] = min_c
            
            if min_c == amount + 1:
                return -1 
            else:
                return min_c  

        return helper(amount)