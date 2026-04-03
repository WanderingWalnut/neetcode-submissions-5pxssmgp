class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Add asteroids going right to stack (positive integers)
        # When we encounter a negative asteroid we pop till 
        # left going asteroid is destroyed
        # when popping (destorying asteroids) compare abs values
        # Monotonic increasing stack --> looking for next smaller element

        stack = []

        for astr in asteroids:
            
            # If collision happens
            while stack and stack[-1] > 0 and astr < 0:
                
                # Astr is equal
                if abs(astr) == stack[-1]:
                    stack.pop()
                    break
                
                # L-Astr is greater than right astr
                elif abs(astr) > stack[-1]:
                    stack.pop()
                    continue
                
                # L-Astr is less than right astr 
                else:
                    break
            
            # If not a collision add to stack
            else:
                stack.append(astr)
          
        return stack
                
        