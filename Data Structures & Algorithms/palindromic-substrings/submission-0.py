class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def pali(l, r):
            count = 0 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count 
            
        total = 0

        for i in range(len(s)):
            odd = pali(i, i)
            even = pali(i, i + 1)
            total = total + odd + even 

        return total