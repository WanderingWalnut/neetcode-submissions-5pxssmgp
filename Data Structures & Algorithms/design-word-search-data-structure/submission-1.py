class PrefixNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        # Same as regular prefix tree
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = PrefixNode()
        
            cur = cur.children[ch]
        cur.isWord = True # Last letter of the word

    def search(self, word: str) -> bool:
        # If it's a . check all possible letters from that level
        # for ".ay" check ay from all possible first letters
        # 2 paths, itertaive and recurisve
        cur = self.root

        def dfs(i, cur):
            
            # End of word
            if i == len(word):
                return cur.isWord
            
            ch = word[i]
            
            # Recursive case
            if ch == ".":
                # Check all paths
                for ch in cur.children:
                    print(f"Checking all paths, current {ch}")
                    # If any returns the entire word
                    if dfs(i+1, cur.children[ch]):
                        return True
                return False

            else:
                # Iterative case
                if ch not in cur.children:
                    print(f"{ch} is not part of Trie")
                    return False
                else:
                    print(f"Correct sequence, next char is one of {cur.children}")
                    return dfs(i+1, cur.children[ch])

        return dfs(0, cur)
        



   
                


        

        
