from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Same process but instead of returning True or False we return the path
        # Turn into adjacency list, traverse the list and then turn the visited set into a list and return

        courseMap = defaultdict(list)
        
        for c,p in prerequisites:
            courseMap[c].append(p)
        
        print(courseMap)

        seen = set()
        path = set()
        res = []

        def dfs(course):
            # Base case
            if course in seen:
                return True

            # Cycle detected, return empty []
            if course in path:
                print(f"{course} has a cycle")
                return False

            path.add(course)
            for nbor in courseMap[course]:
                # If a cycle is detected return an empty arr
                if not dfs(nbor):
                    print(f"Detected cycle on {nbor}, return False")
                    return False
            
            path.remove(course)
            
            # Course is marked as safe, no cycles
            seen.add(course)
            res.append(course)

            return True

        
        for i in range(numCourses):
            if not dfs(i):
                print(f"Cycle detected, returning empty arr as ans")
                return []
        
        return res


                  






        