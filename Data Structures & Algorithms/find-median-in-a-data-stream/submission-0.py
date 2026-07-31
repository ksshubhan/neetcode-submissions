from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.min_h = []
        heapify(self.min_h)
        self.max_h = []
        heapify(self.max_h)

    def addNum(self, num: int) -> None:
        if not self.min_h:
            heappush(self.min_h, num)
        elif num > self.min_h[0]:
            heappush(self.min_h, num)
        else:
            heappush(self.max_h, -1 * num)
        
        if (len(self.min_h) - len(self.max_h)) > 1:
            n = heappop(self.min_h)
            heappush(self.max_h, -n)
        elif (len(self.min_h) - len(self.max_h)) < -1:
            n = heappop(self.max_h)
            heappush(self.min_h, -n)
 
    def findMedian(self) -> float:
        res = 0
    
        if len(self.min_h) == len(self.max_h):
            res = (self.min_h[0] + (-1 * self.max_h[0])) / 2
        elif len(self.min_h) > len(self.max_h):
            res = self.min_h[0]
        else:
            res = -1 * self.max_h[0]
        
        return res
        