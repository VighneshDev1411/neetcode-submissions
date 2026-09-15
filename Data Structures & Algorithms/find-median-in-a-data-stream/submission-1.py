class MedianFinder:
    def __init__(self):
        self.mx = []
        self.mn = []
        

    def addNum(self, num: int) -> None:
        if not self.mx or num <= -self.mx[0]:
            heapq.heappush(self.mx, -num)
        
        else:
            heapq.heappush(self.mn, num)

        if len(self.mx) > len(self.mn) + 1:
            heapq.heappush(self.mn, -heapq.heappop(self.mx))
        elif len(self.mn) > len(self.mx):
            heapq.heappush(self.mx, -heapq.heappop(self.mn))


    def findMedian(self) -> float:
        if len(self.mn) == len(self.mx):
            return (-self.mx[0] + self.mn[0]) / 2.0
        
        return float(-self.mx[0])

        
        