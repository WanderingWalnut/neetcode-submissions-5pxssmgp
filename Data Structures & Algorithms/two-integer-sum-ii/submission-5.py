class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Start a pointer at the beginning and one at the end
        # Compare sum, if sum is less than
        # than move left pointer
        # Otherwise right


        l = 0
        r = len(numbers) - 1
        res = []

        while l < r:
            sumNums = numbers[l] + numbers[r]
            print(sumNums)
            if sumNums == target:
                res.append(l+1) # 1 indexed
                res.append(r+1)
                return res
            
            if sumNums < target:
                l += 1
            else:
                r -= 1

        return res
        
        
        