class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary with count of each element
        # for loop over all nums and populate dictionary
        # Create a while loop with this condition while k != 0
        # Grab max values from dict and return res

        res = []

        count = {}

        # Populate count dict with frequencies
        for i in range(len(nums)):
            current = nums[i]

            if current not in count:
                count[current] = 1
            else:
                count[current] += 1

        print('Count dict before while loop: ', count)

        # Grab K frequent elements
        while k != 0:
            # Returns key based on highest value
            num, freq = max(count.items(), key = lambda x: x[1])
            res.append(num)
            count.pop(num)

            k -= 1
            
        
        return res

        

            


        
             
        