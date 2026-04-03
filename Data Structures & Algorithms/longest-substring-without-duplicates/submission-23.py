from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a window to keep track of chars
        # If char already in set remove from the end till window is valid
        # At each step update max window size
        # "zxyzxzz", "xxxx"

        if not s:
            return 0
        if len(s) == 1:
            return 1

        max_substring = 1
        char_count = defaultdict(int)
        l = 0

        for r in range(len(s)):
            cur_char = s[r]
            window = s[l:r]

            if cur_char not in window:
                max_substring = max(max_substring, r-l+1)
                char_count[cur_char] += 1
                print(f"{s[l:r+1]} and {max_substring} and {char_count}")
            
            else:
                char_count[cur_char] += 1
                while l < len(s) and char_count[cur_char] > 1:
                    print(f'Cur char is {cur_char} and s[l] is {s[l]} and l is {l} and {char_count}')
                    char_count[s[l]] -= 1
                    l += 1
        
        return max_substring


