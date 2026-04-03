# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Have a delimeter for each val
        # Null nodes can be N
        # Ex: 1,2,3,Null,Null,4,5 would be 1#2#3#N#N#4#5#

        res = []

        # Pre order traversal, so building back up is easier
        def dfs(root):
            nonlocal res

            if not root:
                strVal = "N#"
                res.append(strVal)
                return 
            
            strVal = str(root.val) + "#"
            print(f"Appending the following to res: {strVal}")
            res.append(strVal)

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res = ''.join(res)
        print(f"Final serialized str: {res}")
        return res
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = list(data.split("#"))
        data = data[:len(data)-1] # Do not include the last empty char spot
        print(data)

        index = 0

        def dfs():
            nonlocal index
            if index >= len(data):
                return None
            
            val = data[index]
            index += 1

            if val == "N":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()

        
        
