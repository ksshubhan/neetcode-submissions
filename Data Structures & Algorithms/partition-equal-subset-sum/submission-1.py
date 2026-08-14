class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo = {}

        target = sum(nums) // 2

        def helper(curSum, i):
            if sum(nums) % 2 != 0:
                return False
            if curSum == 0.5 * sum(nums):
                return True
            if i == len(nums):
                return False
            if (curSum, i) in memo:
                return memo[(curSum, i)] 
            
            if curSum + nums[i] > target:
                # must skip
                skip = helper(curSum, i + 1) 
                memo[(curSum, i)] = skip
                return skip
            else:

                # otherwise consider both
                skip = helper(curSum, i + 1)

                n_curSum = curSum + nums[i]
                take = helper(n_curSum, i + 1)
                res = skip or take
                memo[(curSum, i)] = res
                return res
        
        return helper(0, 0)