class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            # base case 1 
            if target == total:
                res.append(subset.copy())
                return
            
            # base case 2
            if total > target or i >= len(nums):
                return
            
            # decision 1
            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()

            # decision 2
            dfs(i + 1, total)

        dfs(0, 0)
        return res