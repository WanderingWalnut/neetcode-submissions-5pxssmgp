class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kCount ={}
        returnedElements = []

        # Grabs the occurence of each num in list
        for i in range(len(nums)):
            current = nums[i]
            if current in kCount:
                kCount[nums[i]] += 1
            else:
                kCount[nums[i]] = 1
        
        # create the return list with the k most frequent elements
        while (k):
            max_value = max(kCount, key= kCount.get)
            kCount.pop(max_value)
            if max_value not in returnedElements:
                returnedElements.append(max_value)
            k -= 1

        return returnedElements
        
        