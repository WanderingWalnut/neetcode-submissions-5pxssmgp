class Solution:
    def isValid(self, s: str) -> bool:
        # Have one ptr at the top of stack and one at the bottom
        # Both should equal each other, if they dont return false

        bracketMap = {"[":"]", "{":"}", "(":")"}
        
        stack = []

        # myMap = {}

        for i in range(len(s)):
            # If open bracket
            if s[i] in bracketMap:
                stack.append(s[i])
            # If close bracket
            else:
                if not stack:
                    return False
                
                # Grab top most bracket
                openBracket = stack.pop()
                
                # If the open bracket doesnt match its corresponding closed bracket 
                if bracketMap[openBracket] != s[i]:
                    return False
        
        return len(stack) == 0
        