class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        s = s.lower()

        n = len(s) # Len of str

        l = 0

        r = n-1 

        while l < r:
            if s[l] != s[r]:
                return False
           
            l += 1
            print(s[l])
            r -= 1
            print(s[r])
        
        return True
        