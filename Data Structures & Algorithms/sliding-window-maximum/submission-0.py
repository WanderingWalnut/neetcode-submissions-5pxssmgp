class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Create our window
        # l = 0, r = k - 1
        # For each window insatnce grab the maximum num
        # Slide over by 1
        # run while r < len(nums)

        l, r = 0, k - 1

        res = []

        while r < len(nums):
            maxNum = max(nums[l:r+1])
            print("Current maxNum: ", maxNum)
            
            res.append(maxNum)

            r += 1
            l += 1
        
        print(res)
        return res


        