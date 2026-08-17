class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # overall maximum sum found so far
        maxSum = nums[0]

        # sum of the current sub array 
        curSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(curSum, maxSum)


        return maxSum
