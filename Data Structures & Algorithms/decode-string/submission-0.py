class Solution:
    def decodeString(self, s: str) -> str:
        # Iterate through the str
        # Add each char
        # If char is a num, run a while loop
        # Add for k times
        # return str

        stack = []
        currStr = ""

        num = 0

        for char in s:
            
            if char.isdigit():
                num = num * 10 + int(char) # Handles multi-digit nums
            
            # Beginning of a sequence
            elif char == '[':
                stack.append([currStr, num])
                currStr = ""
                num = 0
            
            # End of a sequence
            elif char == ']':
                prev_str, k = stack.pop()
                currStr = prev_str + currStr * k
            
            # Add just non-sequence char's
            else:
                currStr += char
        
        return currStr

        
