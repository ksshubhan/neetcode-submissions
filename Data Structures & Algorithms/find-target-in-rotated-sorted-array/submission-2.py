class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1      
        
        # Find pivot / minimum
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot_index = l

        # Choose the correct sorted half
        if nums[pivot_index] <= target <= nums[-1]:
            l = pivot_index
            r = len(nums) - 1
        else:
            l = 0
            r = pivot_index - 1
        
        # Normal binary search
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1