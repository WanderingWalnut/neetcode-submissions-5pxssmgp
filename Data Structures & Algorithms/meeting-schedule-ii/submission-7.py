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
        # Use a min heap based on end time
        # At each step check the top of the heap, if earlist end time
        # Is equal to or after then we dont add to heap
        # At the end, the need for rooms is equal to size of heap

        intervals = sorted(intervals, key=lambda x:x.start)

        min_heap = []

        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            # First iteration just add to min_heap
            if not min_heap:
                heapq.heappush(min_heap, [end, start])
                continue

            # If current meeting start is before the earliest end, add room
            if start < min_heap[0][0]:
                heapq.heappush(min_heap, [end, start])
            # If current meeting starts after, replace the old meeting
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, [end, start])


        
        return len(min_heap)




