class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # If an element appears more than ⌊ n/3 ⌋ 
        # we add it to the res list
        # e.g if len(nums) = 10 --> n/3 --> 3
        # if any element appears more than 3 times add to list
        # Solution:
        # Similar to Majority Element I
        # Create a dict, store counts
        # Create one for loop for counts and one for creating res
        # On res loop, check each count and if appears more than
        # Threshold add to res


        res = []
        count = {}
        thres = len(nums)//3
        print("Len of nums: ", len(nums))
        print("Threshold: ", thres)

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        print("Count Dict: ", count)
        
        for i in range(len(nums)):
            if count:
                current = max(count, key=count.get)
                print("Key:", current)
                print("Value: ", count[current])
                if count[current] > thres:
                    res.append(current)
                    print("Result Array: ", res)
            
                count.pop(current)
        
        return res
        