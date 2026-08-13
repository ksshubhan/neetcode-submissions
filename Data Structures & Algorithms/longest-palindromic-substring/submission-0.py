class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def pali(l, r):
            pali_s = ""
            while l >= 0 and r < len(s) and s[l] == s[r] :
                pali_s =  s[l:r+1]
                l -= 1
                r += 1
            return pali_s

        max_p = ""
        odd = ""
        even =  ""
        for i in range(len(s)):
            odd = pali(i, i)
            even = pali(i, i + 1)
            if len(odd) > len(even) and len(odd) > len(max_p):
                max_p = odd
            elif len(even) > len(odd) and len(even) > len(max_p):
                max_p = even
            
        return max_p