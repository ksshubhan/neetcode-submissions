class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            count = 0
            while i != 0:
                if 1 & i == 1:
                    count += 1
                i = i >> 1
            res.append(count)
        
        return res 




