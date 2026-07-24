class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 

        # we want A to be the smaller array at all times
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        # we use the +1 for odd numbers
        # even is fine even with this becasue the // floors the 1 
        half = (total + 1) // 2 

        # we need to use binary search to partion the array
        l, r = 0, len(A)
        
        while l <= r:
            i = l + (r - l) // 2
            j = half - i 

            # 4 edges cases one of the each may not exist 
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')

            # we need to make sure the partition is valid
            # everything on the left is safely below everything on the right
            if Aleft <= Bright and Bleft <= Aright:
                total = len(A) + len(B)
                
                if total % 2 != 0:
                    median = max(Aleft, Bleft)
                else:
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2

                return median

            elif Aleft > Bright:
                # there are too many elements from A
                r = i - 1 
            
            else:
                # there are too few elements from A
                l = i + 1




        