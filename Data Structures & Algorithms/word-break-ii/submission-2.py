class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # We need all possible valid sentences, so use backtracking
        # At each index, try every possible substring starting from that index
        # If the substring is a valid word, add it to our current path
        # Then recurse on the remaining suffix of the string
        # When we reach the end of s, join the chosen words into a sentence
        # and add it to the result

        res = []
        wordDict = set(wordDict)

        def backtracking(i, path):
            if i == len(s):
                res.append(" ".join(path))
                return
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    path.append(word)
                    backtracking(j+1, path)
                    path.pop()
        
        backtracking(0, [])
        print(res)
        return res