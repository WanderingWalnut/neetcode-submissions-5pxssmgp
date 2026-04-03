class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse the array 
        # upto index k is the swapped elemenets (back) reverse them
        # n - k to the end is the rest of the array (front), reverse them

        k %= len(nums)
        nums.reverse()
        print(nums)

        end = k - 1
        i = 0
        # Reverse back half
        while i < end:
            nums[i], nums[end] = nums[end], nums[i]

            i += 1
            end -= 1

        print("Value of K: ", k)
        # Reverse front half
        end = len(nums) - 1
        start = k
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1
        
        print(nums)


        
        
        

            


        