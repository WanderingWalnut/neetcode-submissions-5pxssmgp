class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack keeps all nums/scores
        # When we come across a special character
        # Apply its func on the stack nums 

        record = 0
        stack = []

        for ops in operations:
            # Add the 2 scores together
            if ops == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                record += score
                print("Add 2 elements: ", stack, record)

            elif ops == "C":
                # Remove element & update score
                score = stack.pop()
                record -= score
                print('Remove 1 element: ', stack, record)
            
            elif ops == "D":
                # Double top most element
                score = stack[-1] * 2
                stack.append(score)
                record += score
                print("Double top element: ", stack, record)
            else:
                stack.append(int(ops))
                record += (int(ops))
        
        return record

            
                
        