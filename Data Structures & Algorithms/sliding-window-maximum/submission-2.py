class Solution:
    # came up with the solution by myself however could be more efficient!
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initialise res which will store our list of max values
        res = []

        # initialise the left pointer
        l = 0
        
        # iterate through nums
        for r in range(len(nums)):
            # because we have a fixed window size on each iteration 
            # we check if the window size is equal to k 
            if r - l + 1 == k:
                # if it is we take the maximum number in our current window
                # and add it to res
                res.append(max(nums[l:r+1]))
                # we then increment the left pointer
                l += 1
        
        # at the end we return our list of max values
        return res