class Solution:
    # Their solution which is more efficient and uses a queue
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initialing array to store max_values
        res = []

        # initialising left pointer
        l = 0

        # we initalise a double ended monotonic decreasing queue
        # double ended queue means we can add and remove from both ends
        # in this we will store the indices not the numbers themselves
        queue = collections.deque()
        
        # iterate through nums (our list of numbers)
        for r in range(len(nums)):
            # IMPORTANT: we use a queue because its operations are O(1)
            # this allows us to achieve and overall complexity of O(n)
            # while the queue is not empty and the back of the queue is less 
            # current value in nums
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop() # remove from the back of the queue
            queue.append(r) # then we add the value of r 

            # if our left pointer index is greater than the index stored at 
            # left of the queue then we remove the index at the left of queue
            # because the left pointer has moved on so the index at the left 
            # of the queue is too old
            if l > queue[0]:
                queue.popleft()
            
            # if the size of our window is the same as k 
            # we add the item at the front of the queue because it will
            # always be the biggest
            if r - l + 1 == k:
                res.append(nums[queue[0]])
                # then we increment left pointer
                l += 1
        
        # at the end we return our list of max values
        return res
                