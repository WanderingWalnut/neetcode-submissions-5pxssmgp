class Solution:

    def encode(self, strs: List[str]) -> str:
        encStrs=""
        for word in strs:
            encStrs += str(len(word)) + "#" + word
        return encStrs
        
    def decode(self, s: str) -> List[str]:
        decStrs, i =[], 0
        
        while i<len(s):
            str_begin = s.find("#", i) #find position of string begin
            length = int(s[i:str_begin]) #length of string
            decStrs.append(s[str_begin + 1: length + str_begin + 1])

            i = str_begin + 1 + length

        return decStrs
        
            



            

        
