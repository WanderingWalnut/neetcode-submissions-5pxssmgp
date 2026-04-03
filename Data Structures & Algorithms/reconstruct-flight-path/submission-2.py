from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Sort the list of tickets 
        # Create an adjacency list
        # DFS and traverse, add each one to res
        # If seen skip

        tickets.sort()
        adjList = defaultdict(list)
        
        # Map each origin to all it's arrivals
        for org, arr in tickets:
            adjList[org].append(arr)

        res = ["JFK"]

        def dfs(src):
            # 
            if len(res) == len(tickets)+1:
                return True
            
            if src not in adjList:
                return False
            
            # Create a snapshot
            temp = list(adjList[src])
            # Iteratve over the index and the value (neighbours)
            for i, v in enumerate(temp):
                # Recursively check all paths
                adjList[src].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                
                # Backtrack if inavlid path
                adjList[src].insert(i, v)
                res.pop()
            
            return False
            
        dfs("JFK")
        return res