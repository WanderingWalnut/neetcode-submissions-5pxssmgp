class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Each boat is max 2 ppl
        # Max weight is 6
        # Find min amount of boats
        # Brute force would be for every weight[i]
        # Check all other weights
        # Use 2 ptr for optimized, but how do we move our wndw?
        # What is a valid min boat?
        # Sort the array
        # Start from left and right
        # If sum is under target, valid boat
        # If too big move r and vice versa
        # store as a tuple in a set called onBoat

        res = 0
        people = sorted(people)
        
        print(people)
        l, r = 0, len(people) - 1

        while l < r:
            print("Processing people's: ", people[l], people[r])
            totalWeight = people[l] + people[r]
            # If total weight is less than limit ship together
            if totalWeight <= limit:
                res += 1
                l += 1
                r -= 1
            # Heaviest has to go alone
            else:
                res += 1
                r -= 1
        print(" Current Ptr Pos: ", l, r)
        # Add the last remaining person
        if r - l == 0:
            res += 1

        return res


        

        