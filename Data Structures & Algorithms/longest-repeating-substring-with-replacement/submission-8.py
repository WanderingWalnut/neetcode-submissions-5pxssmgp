from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a window, use a for loop
        # i increase our window
        # l decreases our window
        # We decrease once our substring has K distinct elements
        # Use a dictionary labelled freq, keeps track of our char frequency
        # in our window
        # If freq has more than 2 inputs (elements)
        # and the min value from the dict is greater than K
        # Move left ptr till it becomes valid again

        freq = defaultdict(int)
        res = 0
        l = 0

        for r in range((len(s))):
            freq[s[r]] += 1
            print(len(freq))

            max_freq = max(freq.values())
            window_size = r - l + 1

            # Our window has more distinct elements than we should ahve
            if window_size - max_freq > k:
                # change = min(freq.values())
                # print("Change is: ", change)
                
                # Decrease till we become valid again
                while window_size - max_freq > k:
                    freq[s[l]] -= 1
                    max_freq = max(freq.values())
                    l += 1
                    window_size = r-l+1
                    # change = min(freq.values())
            
            res = max(res, r-l+1)
        
        return res
            
                
            
       
            
            





        