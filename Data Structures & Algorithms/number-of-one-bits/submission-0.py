class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if 1 & n == 1:
                count += 1
            n = n >> 1
        
        return count