class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()
        return clean_s == clean_s[::-1]


        