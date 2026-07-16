class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create data structure to store positions and their index 
        # before sorting

        # create a stack to store the fleets
        res = []
        stack = []

        # now we need to create a way to store the car positions in 
        # descending order but have the corresponding indexes to access their
        # relevant speeds
        # so we enumerate the position and its index and add it to our
        # array
        # then we sorted our res array of tuples based on the first value which
        # will the positions so we get the positions in descending order
        
        for i, p in enumerate(position):
            res.append([p, i])
        sorted_res = sorted(res, key=lambda x: x[0], reverse=True)

        for i in sorted_res:
            # for each car we calculate how long it takes to reach target
            time = (target - i[0]) / speed[i[1]]

            # we push this time onto the stack
            stack.append(time)
            # len(stack >= 2) - there must be at least two arrival times to compare
            # stack[-1] <= stack[-2]
            # stack[-2] is the element after stack[-1] because stack[-1]
            # is the top of the stack so if the condition is true then it means
            # car in stack[-1] car will arrive at the same time as stack[-2] car
            # because it will have to slow down
            # so we pop off stack[-1] because the time it will arive will be the same as stack[-2]
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)