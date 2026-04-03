class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isWord = False        

    def insert(self, word: str) -> None:
        # Insert all letters, mark the last one as isWord = True
        
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = PrefixTree()
            node = node.children[ch]
        
        # Update last letter to be True
        node.isWord = True
        

    def search(self, word: str) -> bool:
        # Find the first letter and build from there

        node = self

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        # Just search for prefix, if nothing is missing return True

        node = self

        for ch in prefix:
            if ch not in node.children:
                return False
            
            node = node.children[ch]
        
        return True
        
        