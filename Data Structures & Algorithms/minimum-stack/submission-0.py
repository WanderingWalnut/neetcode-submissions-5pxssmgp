import math
class MinStack:

    def __init__(self):
        # Create 2 stacks, one for min num and one for all nums
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print('Pushed: ', val)

        # If list is empty or new val is less than the top most element
        if not self.min_stack or val <= self.min_stack[-1]:
            print("Adding new num to min stack: ", val)
            self.min_stack.append(val)


    def pop(self) -> None:
        removed = self.stack.pop()
        
        # If top most element is the smallest element as well
        if removed == self.min_stack[-1]:
            self.min_stack.pop()
            print("New Min Stack: ", self.min_stack)
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]


        


        
