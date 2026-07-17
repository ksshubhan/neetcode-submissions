class Solution:
    # the main idea: number of replacements needed = window length - 
    # frequency of most common character
    # e.g. in AABAC: the window length is 5, the most common character is A
    # 5 - 3 = 2. If k >= 2 then this window is valid


    def characterReplacement(self, s: str, k: int) -> int:
        # Here we store how many times each character appears 
        # in the current window
        count = {}
        
        # we store the current longest length of the window we have found 
        # so far
        res = 0 
        
        # Initialise left pointer
        l = 0

        # right pointer is created by the loop
        for r in range(len(s)):
            
            # Here we add the occurences of the right pointer character
            # if this is the first occurence then the count is 0
            # otherwise we get the present count of the character
            # and add 1 to it
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # if the window length - most commonly occuring character is more than k
            # we don't have enough replacements to replace all the necessary characters
            # so the window is not valid 
            # we are removing a character so we need to reduce the frequency count
            # of the character by 1
            # then we shift the left pointer by 1 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # we compare the current length of the window with the max_value
            res = max(res, r - l + 1)
        
        # at the end we return the longest length of the window we could find
        return res
        