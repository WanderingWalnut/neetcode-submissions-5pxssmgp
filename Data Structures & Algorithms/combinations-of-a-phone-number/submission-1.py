class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case is i == len(digits)
        # For each digit create all combinations
        # ex for 3,4 we iterate over def and create all combos
        # Our constraint is the size which is a maximum of 4

        letterMap = {"2":"abc", "3": "def", "4":"ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        
        if not digits:
            return []


        def dfs(i, part):
            # Base case
            if i == len(digits):
                combo = "".join(part)
                print(f"Adding {combo}")
                res.append(combo)
                return
            
            for j in range(0, len(letterMap[digits[i]])):
                ch = letterMap[digits[i]][j]
                if len(part) <= 4:
                    part.append(ch)
                    print(f"Trying {part}")
                    dfs(i+1, part)
                    part.pop()
        
        dfs(0, [])
        return res




        