class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return -1

        result = [-1] * len(queries)
        heap = []
        intervals.sort(key=lambda x:x[0])
        sorted_idx = sorted(range(len(queries)), key=lambda i:queries[i])

        i = 0
        for idx in sorted_idx:
            q = queries[idx]
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[idx] = heap[0][0]

        return result

        