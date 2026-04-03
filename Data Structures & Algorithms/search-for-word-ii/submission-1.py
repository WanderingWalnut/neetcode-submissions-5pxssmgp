class PrefixNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()
    
    def addWord(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = PrefixNode()
            
            cur = cur.children[ch]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build off word search I
        # Now we have to find words instead of word
        # So we can't just create a backtracking function starting from each letter
        # We have to find ALL the words possible

        ROWS, COLS = len(board), len(board[0])
        res = []
        trie = PrefixTree()
        pathSet = set()

        for word in words:
            print(f"Adding {word} to trie")
            trie.addWord(word)
        
        def dfs(r, c, cur, path):
            # If the letter matches the beginning recursively find the word
            
            # If it is a word, add to output
            if cur.isWord:
                res.append(path)
                cur.isWord = False # So we don't get duplicates
                print(f"Adding {path} to res")
            
            # Inavlidating cases
            if r >= ROWS or c >= COLS or c < 0 or r <0 or (r,c) in pathSet:
                return
            
            ch = board[r][c]
            
            if ch in cur.children:
                pathSet.add((r,c))
                path += ch
                # print(f"Checking all paths from {path}")
                
                # If any direction gives us a valid answer, append to res
                dfs(r+1, c, cur.children[ch], path)
                dfs(r-1, c, cur.children[ch], path) 
                dfs(r, c+1, cur.children[ch], path)
                dfs(r, c-1, cur.children[ch], path) 

                pathSet.remove((r,c))
            
        # Check all possible solutions from all paths
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return res


