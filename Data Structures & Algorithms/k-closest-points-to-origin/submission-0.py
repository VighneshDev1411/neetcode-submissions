class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDistance(x1, y1, x2, y2):
            return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        
        heap = []

        for x, y in points:
            distance = findDistance(0, 0, x, y)

            heapq.heappush(heap, (-distance, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        result = []
        for dist, x, y in heap:
            result.append([x, y])
        return result
        