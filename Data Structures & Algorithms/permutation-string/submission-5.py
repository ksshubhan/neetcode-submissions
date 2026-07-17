class Solution:
    # Solved on my own!
    # then we keeping going through the string until the size of our window
    # is = to our window size
    # then we keeping going through the string until the size of our window
    # is = to our window size
    # now we can check if the characters in that window are a permutation of
    # our substring s1 using sorted because abc and cab become[a, b, c] == [a, b, c]
    # if this is the case we return true 
    # else we slide the left pointer once and check again
    # if we slide all the way to end without finding a permutation
    # then we return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # then we keeping going through the string until the size of our window
        # is = to our window size
        window_size = len(s1)
        l = 0

        for r in range(len(s2)):
            if (r - l) + 1 == window_size:
                if sorted(s2[l:r+1]) == sorted(s1):
                    return True
                else:
                    l += 1
        
        return False 
