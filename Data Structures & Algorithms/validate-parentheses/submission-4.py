class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack, check bracket if it corresponds to LIFO structure
        stack = []

        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If its an open bracket add to stack
            if char in bracket_map.values():
                stack.append(char)
                print("Stack currently: ", stack)
            else:
                # If its a closing bracket
                if char in bracket_map.keys():
                    # And stack is not empty
                    if not stack or stack.pop() != bracket_map[char]:
                        return False
        return not stack

        