class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force solution would be to check for every day all future days
        # O(n^2) solution
        # Iterate through all daily temps
        # Have a stack with all the temps
        # On each day, run a while loop (while stack) --> increment days 
        # if popped > current --> res.append(days)
        # else if stack becomes empty, append(0)

        res = [0] * len(temperatures) # Pre fill with 0's
        stack = []

        i = len(temperatures) - 1

        for i, t in enumerate(temperatures):
            # Pop days from the stack where today's temperature is warmer
            # For each, record how many days it took to reach today's warmer temperature
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index

            stack.append([t, i])
        
        return res

            

    


            





        