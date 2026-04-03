class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Output = []
        total = 1
        zero_count = 0
        arrayLen = len(nums)

        for num in nums:
            if (num == 0):
                zero_count += 1
            else:
                total *= num
        for i in range(arrayLen):
            if (zero_count >= 2):
                Output.append(0)
            if (zero_count == 1):
                if (nums[i] == 0):
                    Output.append(total)
                if (nums[i] != 0):
                    Output.append(0)
            if (zero_count == 0):
                Output.append(total//nums[i])

        return Output



            