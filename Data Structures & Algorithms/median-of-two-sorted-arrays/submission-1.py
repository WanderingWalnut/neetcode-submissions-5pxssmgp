import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure we always use the smallest list
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            # Indices of each array
            i = (l+r) // 2
            j = half - i - 2

            # L and R ptrs within each array
            Aleft = A[i] if i>= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            # Ensure everything on the left half is smaller than everything on the right half 
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    # If odd num of elements, return min between biggest in A and smallest in B
                    return min(Aright, Bright)
                # Otherwise return the median between biggest left parition num and smallest from right partition
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            # Biggest element in partition A is bigger than smallest element in out of parition B
            elif Aleft > Bright:
                r = i - 1
            # 
            else:
                l = i + 1






                    








        