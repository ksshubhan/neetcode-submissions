class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create our list of lists that will store the triplets
        triplets = []
        # we can use .sort() like this to sort the numbers
        # in ascending order
        nums.sort()

        for i, a in enumerate(nums):
            # this condition allows us to check for duplicates
            # i > 0: makes sure we are not at the first element
            # because there will be no previous element to compare it to
            #  a == nums[i - 1] allows to check if our current element
            # is the same as the previous element i.e duplicate
            # if this is the case then we just continue
            if i > 0 and a == nums[i - 1]:
                continue
            
            # we set l to i + 1 because the two pointers should only
            # search the part of the list after i
            l, r = i + 1, len(nums) - 1
            # as long as l < r it means there are still pairs of numbers to test
            # if l == r or l > r then it means we have exhausted all possible pairs of numbers 
            while l < r:
                total = a + nums[l] + nums[r]
                # if the total > 0 then we need to reduce the total 
                # so we decrement r pointer to a smaller value since
                # we're in ascending order
                if total > 0:
                    r -= 1

                # if the total > 0 then we need to reduce the total 
                # so we decrement r pointer to a smaller value since
                # we're in ascending order
                elif total < 0:
                    l += 1
                # if the first 2 conditions aren't true then total must be 0
                # so we add the list of 3 numbers to triplets
                else:
                    triplets.append([a, nums[l], nums[r]])
                    # we increment left pointer and decrement right pointer 
                    # to avoid the pair of numbers that got us the triplet
                    l += 1
                    r -= 1

                    # but it might be the case when we do this we the pointers
                    # land at the same number so we need to continue incremenenting
                    # and decremeting l and r until they are not the same and l < r
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return triplets