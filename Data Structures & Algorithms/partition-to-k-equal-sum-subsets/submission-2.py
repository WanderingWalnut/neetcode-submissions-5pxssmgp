class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Similar to matchsticks but think buckets
        # We can create [0] * k buckets
        # And we can basically try all combinations of buckets that fit where they are all equal
        # Our target for each bucket is sum(nums) / k
        # Ordered descending to catch errors early and fail faster

        nums.sort(reverse=True)  # Sorting in descending order helps prune earlier
        target = sum(nums) / k
        print(f"Target is {target}")

        # If the total sum cannot be evenly divided by k, return False
        if not target.is_integer():
            print(f"Target is not divisible equally by {k}")
            return False

        # Convert target to integer to avoid floating point comparison issues
        target = int(target)
        buckets = [0] * k

        # Early pruning: if the largest number is bigger than the target bucket sum, it can't fit
        if nums[0] > target:
            return False
        
        # Backtracking function to try placing nums[i] into any valid bucket
        def backtrack(i):
            # Base case: all numbers have been placed
            if i == len(nums):
                # Check if all buckets are filled exactly to target
                return all(b == target for b in buckets)
            
            used = set()  # Tracks bucket states we've already tried for this number

            for j in range(k):
                # Skip trying this bucket if we've already tried a bucket in the same state
                if buckets[j] in used:
                    continue

                # Only proceed if placing nums[i] doesn't overflow the bucket
                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]  # Place the number in the bucket

                    # Recurse to place the next number
                    if backtrack(i + 1):
                        return True

                    # Backtrack: remove the number and try another bucket
                    buckets[j] -= nums[i]
                    used.add(buckets[j])  # Mark this bucket state as tried
            
            # If no bucket placement worked, return False
            return False
        
        # Start placing numbers from index 0
        return backtrack(0)
