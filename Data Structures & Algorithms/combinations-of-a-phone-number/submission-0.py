class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case is if i == len(digits)
        # For each letter in the first digit create combinations with the rest
        # Create a hashmap that maps each digit to it's relavent letters

        letterMap = {"2":"abc", "3": "def", "4":"ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        
        def backtrack(i, cur):

            if i >= len(digits):
                res.append(cur)
                return
            
            for char in letterMap[digits[i]]:
                backtrack(i+1, cur + char)
        
        # Only start the function if digits is not empty
        if digits:
            backtrack(0, "")

        
        return res 
        