class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        i= 0

        length = len(numbers)
        left = 0
        right = length - 1

        while left < right:
            sumNum = numbers[left] + numbers[right]

            if sumNum == target:
                return [left+1, right+1]
            elif sumNum > target:
                right -= 1
            else:
                left += 1

        return []