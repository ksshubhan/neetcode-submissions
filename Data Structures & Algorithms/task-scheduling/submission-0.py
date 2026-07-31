from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map = {}
        queue = []
        time = 0
        h = []
        heapify(h)

        for letter in tasks:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        
        # storing first frequency, actual character then cool down time
        for x in hash_map:
            heappush(h, (-hash_map[x], x))
        
        while h or queue:
            time += 1
            if h:
                frequency, char = heappop(h)
                frequency += 1
                if frequency != 0:
                    queue.append([char, frequency, time + n])
            if queue:
                if time == queue[0][2]:
                    heappush(h, (queue[0][1], queue[0][0]))
                    queue.pop(0)
        
        return time