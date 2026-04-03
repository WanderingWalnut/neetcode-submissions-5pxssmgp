class Solution:
    def reorganizeString(self, s: str) -> str:
        # Grab all counts of chars in s
        # If any char has counts > len(s)//2+1, impossible so return ""
        # Lets use a priority queue, each char is added based on when it can come next
        # Input: s = "abbccdd", heap with [0, 1, a], [0, 2, b], ...
        # Grab the the top most element add to our str and then update next index column
        # So if we used "b" then it would turn into [2, 1, b]

        char_count = {}
        for i in range(len(s)):
            ch = s[i]
            char_count[ch] = char_count.get(ch, 0) + 1
        
        max_count = max(char_count.values())
        
        if max_count > len(s)//2 + 1:
            return ""
        
        print(char_count)

        max_heap = []
        for char, count in char_count.items():
            heapq.heappush(max_heap, [-count, char])
        
        res = []
        prev = None
        while max_heap or prev:
            if not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)

            res.append(char)
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]        
        
        print(res)
        return "".join(res)





