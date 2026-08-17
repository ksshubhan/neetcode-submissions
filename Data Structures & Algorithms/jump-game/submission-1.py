class Solution:
    # The solution to this problem involves working backwards
    def canJump(self, nums: List[int]) -> bool:
        # intialise goal as last index 
        goal = len(nums) - 1

        # we iterate through each index and value in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # if the index + the value it holds > greater goal
            # that means we can reach the goal from index we are currently on 
            # because value is just the max steps we can take
            # we can take less than that if need be
            # the only condition we couldn't not reach from current index
            # is if i + nums[i] < goal, because then even the maximum possible jump
            # from this index is not enough to reach the goal.
            if i + nums[i] >= goal:
                    # if we can reach the current goal from this index,
                    # make this index the new goal.
                    goal = i

        # If the goal has moved all the way back to index 0,
        # then index 0 can eventually reach the final index.
        return goal == 0

        