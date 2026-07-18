class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we handle the edge case if no substring exists then we return an
        # empty string
        if t == "": return ""

        # initialise our two hashmaps one for the substring to compare to
        # another for our sliding window
        countT, window = {}, {}

        # the hashmap for our substring will not change so we only need to
        # populate it once
        for c in t:
            # for each character in the string add it to our hashmap
            # if the character is not already present we use a default value
            # of 0
            countT[c] = 1 + countT.get(c, 0)

        # we set our have attribute to 0 because at the start we won't have
        # any of the characters we need
        # we set need to length of countT because the length gives us
        # the number of unique characters in t 
        have, need = 0, len(countT)

        # we initialise... 
        res, resLen = [0, 0], float("infinity")
        
        # we initialise our left pointer
        l = 0

        # now we iterate through the string
        for r in range(len(s)):
            # store the current character in c
            c = s[r]
            # we update our window hashmap to count the character
            window[c] = 1 + window.get(c, 0)

            # IMPORTANT: we check if the character is in countT i.e. our substring
            # and if it is and the counts match then we increment have 
            if c in countT and window[c] == countT[c]:
                    have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = (r - l) + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        