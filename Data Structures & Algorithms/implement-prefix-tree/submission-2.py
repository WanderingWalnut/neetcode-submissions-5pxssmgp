class PrefixNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        # Insert if it's not part of child n traverse
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                print(f"Adding {ch}")
                cur.children[ch] = PrefixNode()
            cur = cur.children[ch]
            print(f"Cur is moving to {cur}")
        
        cur.isWord = True # Set last letter of word to be True

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            print(f"{ch} exists in tree")
            cur = cur.children[ch]
        
        return cur.isWord

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return False
            print(f"{ch} exists in tree")
            cur = cur.children[ch]

        return True # We are looking for prefix not a word
        
        