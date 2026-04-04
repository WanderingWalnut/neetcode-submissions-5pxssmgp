class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Since we need to find all possible sentences, this is backtracking
        # Use backtracking to add len(wordDict)-1 spaces to your s
        # if the sentence has all valid words in word dict, add it to res
        # Return the final output
        # Input: s = "neetcode", wordDict = ["neet","code"]
        # n eetcode, ne etcode, nee tcode, neet code

        res = []
        spaces = len(wordDict)-1

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



        