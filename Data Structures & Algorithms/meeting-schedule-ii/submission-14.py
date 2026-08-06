"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Same like meeting rooms but now we need to keep track of count
        # Each time we have a conflict, do not return false but increment. a counter
        
        intervals = sorted(intervals, key= lambda i:i.start)

        min_heap = []
        rooms = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            if min_heap:
                # We need a new room
                if min_heap[0] > start:
                    heapq.heappush(min_heap, end)
                    rooms += 1
                # We can take an existing room
                else:
                    heapq.heapreplace(min_heap, end)
            # No rooms taken, first meeting
            else:
                heapq.heappush(min_heap, end)
                rooms += 1
        
        return rooms