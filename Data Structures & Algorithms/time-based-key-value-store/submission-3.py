class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Insert values into dictionary

        # If that key entry already exists
        if key in self.timeMap:
            self.timeMap[key]["values"].append(value)
            self.timeMap[key]["timestamps"].append(timestamp)
        # If that key does not exist
        else:
            self.timeMap[key] = {
                "values": [value],
                "timestamps": [timestamp]
            }
        

    def get(self, key: str, timestamp: int) -> str:
        # Run binary search on timestamps
        # Find the timestamp that is equal to or less than timestamp
        # i.e apple : ["Green", 5] and apple : ["Red", 10] 
        # get(apple, 7) would give us "Green"

        # Looking for most recent timestamp so start at the lowest possible

        if key not in self.timeMap:
            return ""
        l, r = 0, len(self.timeMap[key]["timestamps"]) - 1
        res = -1

        while l <= r:

            mid = l + (r-l)//2

            prev_timestamp = self.timeMap[key]["timestamps"][mid]

            # Exact time stamp is present
            if prev_timestamp == timestamp:
                return self.timeMap[key]["values"][mid]
            # prev_timestamp is less than max timestamp, we can try and find a bigger one    
            elif prev_timestamp < timestamp:
                res = max(res, mid)
                l = mid + 1
            # Time stamp is too big
            else:
                r = mid - 1
        
        if res == -1:
            return ""

        return self.timeMap[key]["values"][res]




        
        
