import math
from heapq import heappop, heappush, heapify

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapify(h)
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            d = math.sqrt((x)**2 + (y)**2)
            heappush(h, (-d, [x, y]))
            if len(h) > k:
                heappop(h)
            
        res = [point for distance, point in h]
        return res

