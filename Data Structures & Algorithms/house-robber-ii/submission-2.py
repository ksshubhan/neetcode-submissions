class Solution:
    def rob(self, nums: List[int]) -> int:
        arr1 = [nums[i] for i in range(0, len(nums) - 1)]
        arr2 = [nums[i] for i in range(1, len(nums))]
        rob1_1, rob2_1 = 0, 0
        rob1_2, rob2_2 = 0, 0

        for n in arr1:
            temp_1 = max(n + rob1_1, rob2_1)
            rob1_1 = rob2_1
            rob2_1 = temp_1
        
        for n in arr2:
            temp_2 = max(n + rob1_2, rob2_2)
            rob1_2 = rob2_2
            rob2_2 = temp_2
        
        return max(nums[0], rob2_1, rob2_2)
