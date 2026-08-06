"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # End time of prev meeting overlapping in the start of the next meeting
        # Sort the meetings by start time
        # On the first iteration add the end meeting time to heap
        # On each subsequent instance check the top of the min heap
        # If the earliest end time is greater than the current start time return false

        intervals = sorted(intervals, key= lambda i:i.start)

        min_heap = []

        for item in intervals:
            start = item.start
            end = item.end
            print(start, end)
            if min_heap:
                # If meeting end time greater than current start time
                if min_heap[0] > start:
                    return False
                else:
                    min_heap[0] = end

            else:
                heapq.heappush(min_heap, end)
        
        return True
