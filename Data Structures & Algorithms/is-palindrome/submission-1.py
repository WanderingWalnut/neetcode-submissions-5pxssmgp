class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        connected_string = ""

        for char in s:
            if char.isalnum():
                connected_string += char
        reverse_string = connected_string[::-1] # Reverse string

        if (reverse_string == connected_string):
            return True
        else:
            return False

        


        