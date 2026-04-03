class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Builds on 3-sum, similar concept except we're adding one more num
        # to the mix
        # Possibly same logic and just add another for loop

        nums = sorted(nums)
        res = []
        seen = set()

        if len(nums) < 4:
            return []
        
        if len(nums) == 4:
            sumNums = nums[0] + nums[1] + nums[2] + nums[3]
            if sumNums == target:
                return [nums]
            else:
                return []

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                l = j + 1
                r = len(nums) - 1

                while l < r:

                    sumNums = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    # Total equals target
                    if sumNums == target:
                        # All values are unique
                        if i != j and i != l and i != r and j != l and j != r and l != r:
                            quad = tuple((sorted([nums[i], nums[j], nums[l], nums[r]])))
                            # This solution has not been found
                            if quad not in seen:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                print("Added following set: ", quad)
                                seen.add(quad)
                    
                    if sumNums > target:
                        r -= 1
                    else:
                        l += 1
        return res
        