class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}':'{', ']':'[', ')':'('}

        for char in s:
            # Is it a closing bracket?
            if char in closeToOpen:
                # Does the stack have elements and does the closing bracket match its coressponding open bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            # Add to stack if not a closing bracket
            else:
                stack.append(char)
            
        return True if not stack else False
            

        