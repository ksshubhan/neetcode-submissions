class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        res = []
        size = 0
        start = 0
        end = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in hash_map:
                hash_map[s[i]] = i
        
        for i in range(len(s)):
            end = max(end, hash_map[s[i]])
            if i == end:
                size = end - start + 1
                res.append(size)
                start = end + 1 

        return res
