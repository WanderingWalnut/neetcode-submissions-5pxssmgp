from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Map each user to the list of websites they visited, in timestamp order
        user_visits = defaultdict(list)

        # Zip the three lists together as (time, user, website),
        # then sort by time so each user's visits are in correct order
        for time, user, site in sorted(zip(timestamp, username, website)):
            user_visits[user].append(site)

        # Count how many users have each 3-website pattern
        pattern_count = defaultdict(int)

        # Go through each user's ordered website history
        for user, sites in user_visits.items():
            # Generate all possible 3-website patterns for this user
            # Use a set so the same user only contributes once per pattern
            for pattern in set(combinations(sites, 3)):
                pattern_count[pattern] += 1

        # Track the best pattern seen so far and its count
        best_pattern = ()
        best_count = 0

        # Find the pattern with the highest count
        # If there is a tie, choose the lexicographically smaller pattern
        for pattern, count in pattern_count.items():
            if count > best_count or (count == best_count and pattern < best_pattern):
                best_pattern = pattern
                best_count = count

        # Return as a list because the problem expects List[str]
        return list(best_pattern)