from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Turn word list into a graph
        # Start traversal of graph from node where valid i.e cat -> bat
        # Recursively traverse via DFS and return the count/steps

        # Helper function for validating it is the next valid word
        def isFollowRule(w1, w2):
            differences = 0


            # Uneven lens return False
            if len(w1) != len(w2):
                return False

            # Iterate over each char
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    differences += 1
            
            # More than 1 difference is not allowed
            if differences > 1:
                return False
            
            return differences == 1
        
        if endWord not in wordList:
            return 0
        
        # Create graph of words
        tempWords = [beginWord] + wordList
        adjList = defaultdict(list)

        for i in range(len(tempWords)):
            curWord = tempWords[i]
            # Find all matching words it can traverse to
            for j in range(i+1, len(tempWords)):
                if isFollowRule(curWord, tempWords[j]):
                    print(f"Adding {tempWords[j]} connects to {curWord}")
                    adjList[tempWords[i]].append(tempWords[j])
                    adjList[tempWords[j]].append(tempWords[i])
        
        print(adjList)

        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, dist = q.popleft()

            if word == endWord:
                return dist
            
            for nbor in adjList[word]:
                if nbor not in seen:
                    q.append((nbor, dist+1))
                    seen.add(nbor)
            
        return 0




        