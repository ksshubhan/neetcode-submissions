class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        max_length = 0
        l = 0

        for r in range(len(s)): 
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            length = (r - l) + 1
            max_length = max(length, max_length)

        return max_length