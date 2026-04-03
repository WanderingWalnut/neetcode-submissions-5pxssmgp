class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode each string as follows:
        # len of word is at the beginning
        # '#' is the start of a word
        # ['neet', 'code']
        # Would be 4#neet4#code

        encStr = ""

        # Iterate over each word in list of strs, join and add encoding
        for word in strs:
            encStr += str(len(word))
            encStr += '#'
            encStr += ''.join(word)
            
        # print(encStr)
        return encStr

    def decode(self, s: str) -> List[str]:
        # For char in s
        # first val is len of word
        # '#' is beginning
        # join the word together till we hit num again
        res = []
        i = 0

        while i < len(s):
            lenWord = ""
            # Extract len of word, edge case of multi-digit num
            while i < len(s) and s[i].isdigit():
                lenWord += s[i]
                i += 1

            if i < len(s) and s[i] == "#":
                i += 1 # Skip that iteration
            
            lenWord = int(lenWord) # Convert to int
            word = s[i: i + lenWord] # Create word

            res.append(word)
            i = i + lenWord # Update index to start new word
        return res
            