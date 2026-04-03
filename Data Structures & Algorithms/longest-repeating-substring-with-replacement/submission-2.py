class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Change k char in string and create longest substring
        # use a hashmap to store count of all chars
        # num of replacements = len of string - frequency of the most frequent character

        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l +1)

        return res
            
            





        