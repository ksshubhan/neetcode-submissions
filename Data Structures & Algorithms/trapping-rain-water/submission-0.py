class Solution:
    def trap(self, height: List[int]) -> int:
        # checks if the entire list is empty because no bars
        # means no trapped water so amount of water trapped is 0
        # also prevents errors when accessing array 
        if not height: return 0

        # initialise our two pointers
        l, r = 0, len(height) - 1

        # we store the tallest boundaries we can find in the array 
        # of heights
        leftMax, rightMax = height[l], height[r]

        # store total amount of trapped water
        total = 0

        # include the condition to make sure we have not searched 
        # the whole array 
        while l < r:
            # If this condition is true then it means we focus on the left pointer
            # because the right height boundary will contain whatever the left is so
            # the right height is certain now we need to increment the left pointer
            # to see if we potentially have a new max left height
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                # because the left side is the bottleneck 
                # we only need to consider it because it does not matter if the
                # right side is 10 or 100 water would leak anyway
                # then we have to subtract the current height we are on from the left boundary
                # because we could be at some height, we may not be on the ground
                # if our new height is greater than or the same it becomes a new boundary and holds no water i.e. we get 0
                # or if its less the gap it will hold water which we calculate below and add to total 
                total += leftMax - height[l]
            
            # If this condition is true then it means we focus on the right pointer
            # because the left height boundary will contain whatever the left is so
            # the left height is certain now we need to increment the left pointer
            # to see if we potentially have a new max right height
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                # because the left side is the bottleneck 
                # we only need to consider it because it does not matter if the
                # right side is 10 or 100 water would leak anyway
                # then we have to subtract the current height we are on from the left boundary
                # because we could be at some height, we may not be on the ground
                # if our new height is greater than or the same it becomes a new boundary and holds no water i.e. we get 0
                # or if its less the gap it will hold water which we calculate below and add to total 
                total += rightMax - height[r]
        
        return total