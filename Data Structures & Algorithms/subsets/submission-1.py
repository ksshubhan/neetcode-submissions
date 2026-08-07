class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initialise empty list
        # will store collection of all complete subsets we have found
        res = []

        # will store the current subset we are building
        subset = []


        def dfs(i):
            # if the index is out of bounds
            if i >= len(nums):
                # we add to our res a copy of what the subet looks like
                res.append(subset.copy())

                # this is equivalent of returning null
                return

            # left branch - do we include 
            subset.append(nums[i])
            dfs(i + 1)

            # right branch - do we not include
            subset.pop()
            dfs(i + 1)

        # initial call
        dfs(0)

        # return final result
        return res