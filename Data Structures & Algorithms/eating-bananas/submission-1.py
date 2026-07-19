import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res - 1
        
        while l <= r:
            mid = l + (r - l) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                res = mid
                r = mid - 1

            else:
                l = mid + 1
        
        return res
