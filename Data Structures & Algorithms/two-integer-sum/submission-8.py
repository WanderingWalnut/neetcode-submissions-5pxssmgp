class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create 2 for loops and check if current num (outer loop)
        # matches inner loop nums --> i.e 3 + 4 = target? 3 + 5 = target?
        # If match return index pair

        res = []
        total = 0

        for i in range(len(nums)):
            print(nums[i])
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        res.append(i)
                        res.append(j)
                        return res
        


        
                    
        



                


        