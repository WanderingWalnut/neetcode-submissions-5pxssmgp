from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjlist, use DFS to find if we are able to take course
        # We use DFS since we are looking for valid path not shortest path
        # Also directed graph and can be disjointed so do DFS from all points
        
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visited = set()
        path = set()
        
        def dfs(course):
            if course in path:
                return False
            
            path.add(course)
            
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            
            path.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        
        return True


        