from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Map each task to its counts
        # Then create a max heap based on counts with n and the process name attached
        # Init each process with n e.g (2, "X", n)
        # On each occurence execute a process (subtract 1 from count and increase n by 1 and re-insert node into heap)
        # if or lets call it cycleDiff % n == 0 we execute process otherwise we wait (idle)
        # Update res on each occurence, if a process executes then +1 if a process doesnt then +1
        # Only thing we need to ensure is that cycleDiff % n == 0 when executing
        
        maxHeap = []
        cooldown_queue = deque()
        
        current_time = 0

        counter = Counter(tasks)
        print(counter)

        for k,v in counter.items():
            heapq.heappush(maxHeap, (-v,k)) # Push counts, process and n
        
        print(f"Here is our max heap: {maxHeap}")

        while maxHeap or cooldown_queue:

            if maxHeap:
                curr = list(heapq.heappop(maxHeap))
                print(f"Current node: {curr}")

                # Insert into cool down queue
                if curr[0] < -1:
                    time_ready = current_time + n + 1
                    cooldown_queue.append((time_ready, curr[0]+1, curr[1])) # Add +1 to curr[0] because it's a negative number
                    print(f"Process {curr[1]} going into cooldown till {time_ready}")
            
            # Idle cycle   
            else:
                print(f"Idle Cycle")
            
            current_time += 1 # Increment cycle count
            
            # If an item's cool down is completed, add back to maxheap to be processed for next loop
            while cooldown_queue and cooldown_queue[0][0] <= current_time:
                time_ready, count, task = cooldown_queue.popleft()
                print(f"Readding {task} to heap, cooldown completed")
                heapq.heappush(maxHeap, (count, task))
            
        
            print(f"Our cooldown queue looks as follows for time {current_time}: {cooldown_queue}")
        
        return current_time
                

   