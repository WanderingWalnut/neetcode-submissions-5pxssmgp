class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Base case is when side == 4 and i == len(matchsticks)
        # Each time we have a choice, either extend the sticks or start a new side
        # We have to use all the sticks and we can't split them
        # Has to be a square so all side have to be equal
        # If total is divide by 4 is not even then return false automatically
        # Then for each side it should equal target which is total / 4
        
        matchsticks.sort(reverse=True)# We use descending order to help find earlier failures

        length = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) / 4 != length:
            return False
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            # Try all combinations of squares
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    # Undo prev action
                    sides[j] -= matchsticks[i]
                
            return False
        
        return backtrack(0)

            



        