from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [i * -1 for i in nums]
        heapify(h)
        i = 0
        while i < k:
            res = heappop(h)
            i += 1
        return -1 * res