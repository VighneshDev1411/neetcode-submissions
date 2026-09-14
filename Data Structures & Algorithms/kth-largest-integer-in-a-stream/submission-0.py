import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.pq = []

        for num in nums:
            if len(self.pq) < self.k:
                heapq.heappush(self.pq, num)
            elif self.pq[0] < num: 
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, num)

    def add(self, val):
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
            return self.pq[0]

        if val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)

        return self.pq[0]

