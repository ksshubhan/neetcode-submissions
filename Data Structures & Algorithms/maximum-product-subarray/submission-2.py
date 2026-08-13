class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        max_ending = nums[0]

        min_ending = nums[0]

        for i in range(1, len(nums)):
            n1 = max_ending
            n2 = min_ending
            max_ending = max(n1 * nums[i], n2 * nums[i], nums[i])
            min_ending = min(n1 * nums[i], n2 * nums[i], nums[i])
            new_max = max(max_ending, min_ending)
            res = max(res, new_max)

        return res