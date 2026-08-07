class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, b_set):
            # base case
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            # step case
            for i in range(len(b_set)):
                if b_set[i] == True:
                    subset.append(nums[i])
                    b_set[i] = False
                    dfs(subset, b_set)
                    subset.pop()
                    b_set[i] = True

        dfs([], [True]*len(nums))

        return res