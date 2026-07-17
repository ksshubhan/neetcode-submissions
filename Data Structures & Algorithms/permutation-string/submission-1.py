class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l = 0
        state = []

        for r in range(len(s2)):
            state.append(s2[r])

            if (r - l) + 1 == window_size:
                if sorted(state) == sorted(s1):
                    return True
                else:
                    state.pop(0)
                    l += 1
        
        return False 
