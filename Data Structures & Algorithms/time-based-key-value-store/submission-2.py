class TimeMap:

    def __init__(self):
        self.hash_map = {}
        


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.hash_map:
            l1 = self.hash_map[key]
            target = timestamp
            l,r = 0, len(l1) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if l1[mid][1] <= target:
                    res = l1[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1  
        return res
