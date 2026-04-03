class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Del nums
        # Return len of arr
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]
                print(nums)

        return len(nums)
        