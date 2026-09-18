"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.end)

        if not intervals:
            return True

        curr_end = intervals[0].end
        """
        5 10, 15 20, 0, 30
        """

        for interval in intervals[1:]:
            if curr_end > interval.start:
                return False

            curr_end = interval.end

        return True 
        
