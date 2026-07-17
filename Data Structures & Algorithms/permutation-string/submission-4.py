class Solution:
    # Solved on my own!
    # My idea: since the substring is fixed we know we going to have a fixed
    # length window
    # then we keeping going through the string until the size of our window
    # is = to our window size
    # now we can check if the characters 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 
        window_size = len(s1)
        l = 0
        state = []

        for r in range(len(s2)):
            if (r - l) + 1 == window_size:
                if sorted(s2[l:r+1]) == sorted(s1):
                    return True
                else:
                    l += 1
        
        return False 
