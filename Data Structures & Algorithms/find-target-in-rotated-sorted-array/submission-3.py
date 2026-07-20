class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # intialise pointers
        l, r = 0, len(nums) - 1      
        
        # IMPORTANT: the rotated array will have 2 sorted sections
        # the seperation between these sections is the pivot
        # so we need to find the pivot index
        # for this the pivot is just the minimum value in our array 
        # which we calculated in a prev q, so we can just re-use the same code
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        # l and r both have the same value, they could have been used
        # interchangeably here
        pivot_index = l

        # if our target is between our pivot index and end the of the list
        # then we need to search in the right section
        if nums[pivot_index] <= target <= nums[-1]:
            l = pivot_index
            r = len(nums) - 1
        
        # otherwise our target will be in the left sorted section so we will
        # look in the left sorted section 
        else:
            l = 0
            r = pivot_index - 1
        
        # we perform binary search on correct section 
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        # if we do not find target then we return -1
        return -1