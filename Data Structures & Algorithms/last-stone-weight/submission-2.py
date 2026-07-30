from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones
        h = [i * -1 for i in stones]
        heapify(h)
        while len(h) > 1:
            x =  heappop(h)
            y = heappop(h)
            if x != y:
                heappush(h, -1 * abs(x - y))
        
        res = 0 if h == [] else -h[0]
        return res
