class Solution:
    def simplifyPath(self, path: str) -> str:
        # Go through each char in str
        # Build words/files
        # If we encounter a "/" skip till next valid element
        # If we encounter 2 ".." pop element
        # if we encounter ... or more add it as an element
        # Join the stack elements seperate by / 

        stack = []
        res = ""

        arr = path.split('/')
        print(arr)

        for item in arr:
            
            if item == '':
                # Skip iteration
                continue

            # If its a file labeled "..." or more
            if '.' in item and len(item) == 1:
                continue

            # ".." means pop
            elif '.' in item and stack and len(item) == 2:
                stack.pop()

            # If stack is empty then just skip
            elif '.' in item and not stack and len(item) == 2:
                continue

            # Add words to stack
            else:
                stack.append(item)
                print("Current Stack: ", stack)
        
        
        for folder in stack:
            res += "/" + str(folder) 
        
        if not stack:
            return "/"

        print(res)
        return res





        # for char in path:
        #     word = ""
            

            



        