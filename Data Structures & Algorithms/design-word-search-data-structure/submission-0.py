class WordDictionary:
    # Problem is essentially the same, only change is "."

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        # Same as insert
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            # Iterate forward
            node = node.children[ch]
        
        node.isWord = True

    def search(self, word: str) -> bool:
        # Only difference in this problem is "."
        # Find the remaining word

        def dfs(j, node: WordDictionary):
            cur = node

            for i in range(j, len(word)):
                c = word[i]

                # Recursive case
                if c == ".":
                    # Values are the actual nodes
                    for child in cur.children.values(): 
                        if dfs(i+1, child):
                            return True
                    
                    return False
                
                # Iterative case
                else:
                    if c not in cur.children:
                        return False
                    
                    cur = cur.children[c]
            
            return cur.isWord

        return dfs(0, self)
                


        

        
