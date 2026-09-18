"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
We sort by start time because we need to process meetings in the order they actually begin. If we sort by end time instead, a later meeting could grab a free room before an earlier-starting meeting gets a chance at it — giving the wrong room count.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)
        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval.end)

        return len(heap)












        
        


        