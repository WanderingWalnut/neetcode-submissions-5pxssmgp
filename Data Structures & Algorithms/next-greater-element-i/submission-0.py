class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num1_idx = {}
        for i, num in enumerate(nums1):
            num1_idx[num] = i
        
        print(num1_idx)
        
        stack = []
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            cur = nums2[i]

            while stack and cur > stack[-1]:
                num = stack.pop()
                print(num)
                idx = num1_idx[num]
                res[idx] = cur
            
            if cur in nums1:
                stack.append(cur)
        
        return res


        