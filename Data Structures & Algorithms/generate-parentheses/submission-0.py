class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add open parenthesis when Open >= Closed and Open < n
        # Only add close parenthesis when Closed < Open and Closed < n
        # If Closed == Open == n, append to res and return

        # Holds each parenthesis combination
        stack = []
        res = []

        def backtrack(openN, closedN):
            # Base case
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # Adding open bracket
            if openN < n:
                stack.append('(')
                # Increment open count and recursively call
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # Adding close bracket
            if closedN < openN:
                stack.append(')')
                # Increment open count and recursively call
                backtrack(openN, closedN+1)
                stack.pop()
        
        backtrack(0, 0)
        return res


            




        
        