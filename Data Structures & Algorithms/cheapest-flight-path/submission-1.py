class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj = [i:[] for i in range(n)]

        INF = 10 ** 9

        dist = [INF] * n 
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]

            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w

            dist = temp

        return dist[dst] if dist[dst] != INF else -1





        