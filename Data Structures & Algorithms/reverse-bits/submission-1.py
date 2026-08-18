class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            right_most = 1 & n 
            res = res << 1
            res = res | right_most
            n = n >> 1
        return res 