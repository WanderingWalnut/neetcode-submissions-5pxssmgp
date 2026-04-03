class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Calculate time it takes for each car (target-position)/speed
        # If time is the same then it counts as the same fleet
        # Each fleet is associated with it's time taken
        # Each unqiue time is added to the stack
        
        stack = []

        cars = sorted(zip(position, speed), reverse=True)

        for pos, speed in cars:
            time = (target-pos)/speed

            # First entry add to stack, if time > is greater than the top most element add (new fleet)
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)





        