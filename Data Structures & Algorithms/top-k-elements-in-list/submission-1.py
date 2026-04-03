class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Keep track of occurences 
        count = {}

        ans = []

        #Populate hash map with counts
        for i in range(len(nums)):
            current = nums[i]
            if current not in count:
                count[current] = 1
            else:
                count[current] += 1

        for x in range(k):
            currentMax = max(count, key=count.get) # Grab the current max count
            ans.append(currentMax) # Add highest counts to list for K occurences
            del count[currentMax] #Remove the current max so we get the next most frequent
        
        return ans

        
             
        