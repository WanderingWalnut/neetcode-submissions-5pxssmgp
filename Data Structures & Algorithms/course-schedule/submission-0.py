from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacecny list out of the prerequisites
        # If at anypoint a course needs a previous course then return False
        # Basically checking if there is a cycle then return False
        
        courses = defaultdict(list)

        for p, c in prerequisites:
            courses[c].append(p)
        print(courses)
        
        
        visited = set() # For all safe path's traveresed
        path = set() # For current path, helps detect cycles

        def dfs(course):
            # Cycle detected
            if course in path:
                return False
            
            if course in visited:
                return True
            
            path.add(course)
            # Check all connected paths
            for nbor in courses[course]:
                # If any has a cycle, return false
                if not dfs(nbor):
                    return False
            
            path.remove(course)
            visited.add(course)

            # No cycles detected, return True
            return True
        
        # Call on each course number so that we cover edge case of isolated nodes
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True