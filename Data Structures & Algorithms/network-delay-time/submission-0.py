class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        INF = 10 ** 9

        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = [INF] * (n + 1)
        dist[k] = 0
        pq = ([(0, k)])

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for neighbor, weight in adj[node]:
                if time + weight < dist[neighbor]:
                    dist[neighbor] = time + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        max_time = max(dist[1:])

        return max_time if max_time != INF else -1
        





        