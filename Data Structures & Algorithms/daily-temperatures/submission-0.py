class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:        
        # store results in res - all values are initially set to 0
        # create the stack data structure we need so solve problem
        res = [0] * len(temperatures)
        stack = []
        
        # IMPORTANT: we use enumerate to get the index and temperature at that index
        # because we need to store the values in res
        for i, t in enumerate(temperatures):
            # while stack evaluates to true if non-empty and false if empty
            # because we cannot access stack[-1] if the stack is empty
            # is todays temperature warmer than the temperature at the 
            # top of the stack
            
            # Initially because the stack is empty the while loop is skipped and 73, 0 
            # is added to the stack
            # now we move on to the next t in the for loop: 74
            # the stack is not empty and 74 > 73 so we have found a warmer day
            # so we enter while loop we pop off the stack so 73, 0 is popped of 
            # we then calculate how many days it took to find a warmer day by subtracting
            # the indexes, so i is now 1 from the for loop and stackInd (what we popped of is 0)
            # so 1 - 0 is 1 so 1 day which we store in res
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

