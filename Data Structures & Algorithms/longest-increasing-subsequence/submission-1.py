class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
    
        length = 0

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(nums):
                return 0
            
            if j == -1:
                skip = helper(i + 1, j)
                take = 1 + helper(i + 1, i)
                res = max(take, skip)
                memo[(i, j)] = res
                return res
            
            if nums[i] > nums[j]:
                skip = helper(i + 1, j)
                take = 1 + helper(i + 1, i)
                res = max(take, skip)
                memo[(i, j)] = res
                return res
            else:
                res = helper(i + 1, j)
                memo[(i, j)] = res
                return res

        return helper(0, -1)