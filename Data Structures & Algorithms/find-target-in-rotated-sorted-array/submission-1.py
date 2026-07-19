class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1      
        
        # iterate through list of numbers
        while l <= r:
                # calculate mid point
                mid = l + (r - l) // 2

                # perhaps our midpoint is the target
                # in which we return the index of mid
                if target == nums[mid]:
                    return mid
                
                # if this is not the case we need to check what portion of
                # the array we are in

                if nums[l] <= nums[mid]:
                    if target > nums[mid] or target < nums[l]:
                        l = mid + 1 
                    else:
                        r = mid - 1 
                else:
                    if target < nums[mid] or target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1 
        
        return -1
