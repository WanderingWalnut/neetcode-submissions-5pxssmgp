class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Start one pointer at the beginning and one at the end
        # Move left forward and right backwards, comapre at each iteration
        # If a char doesnt match return false
        # Otherwise return true

        
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()
        print(s)

        l = 0
        r = len(s) - 1

        while l < r:
            print("Current Chars: ", s[l], s[r])
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        