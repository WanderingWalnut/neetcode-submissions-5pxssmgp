class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # We iterate for length s
        # On each iteration we create substrings of size i
        # Each substring is checked if it is a plaindrome
        # If it is then add to res othwerwise continue
        
        res = []
        part = []

        # Check if its a valid palindrome
        def isValid(s):
            if s[::-1] == s:
                print(f"{s} is a valid palindrome, add to res")
                return True
            
            print(f"{s} is not a valid palindrome")
            return False

        def backtrack(i):
            
            # Base case, traveresed the end of str
            if i >= len(s):
                res.append(part.copy())
                return
            
            # We are trying every possible substring i.e "a", "aa", "aab" as a starting point
            for j in range(i, len(s)):
                # If the initial substring is valid
                if isValid(s[i:j+1]):
                    # Add that part to res
                    part.append(s[i:j+1])
                    # Figure out remaining valid parts (substrings)
                    backtrack(j+1)                      
                    part.pop()
            
        backtrack(0)
        return res

        