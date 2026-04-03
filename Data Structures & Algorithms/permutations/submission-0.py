class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Building on previous problems
        # Instead of filtering for repetitive nums we keep them
        # Only difference we have to choose all 3 elements in a solution
        # When i == len(nums), add that as a valid solution
        # Check all combinations till we traverse the entire arr
        # If any of the res has all elements then its a valid permutation
        
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            print(f"Current perm is {p}")
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                print(f"Adding {p_copy} to res")
                res.append(p_copy)
            
        return res