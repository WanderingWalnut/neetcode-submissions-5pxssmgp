import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Add each num to stack
        # When we come across an operatation 
        # Pop the elements and apply operation

        stack = []

        for c in tokens:
            
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[0]
        





        