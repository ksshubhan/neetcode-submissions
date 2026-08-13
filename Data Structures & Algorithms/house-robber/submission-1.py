class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = best amount you could rob up to houses ago
        # rob2 = best amount you could rob up to the previous house
        # initally at the start we have robbed no houses
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2