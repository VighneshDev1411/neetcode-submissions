class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                
                # Calculate Manhattan distance
                x1, y1 = points[i]
                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)

                # Undirected graph → add both directions
                adj[i].append((j, distance))
                adj[j].append((i, distance))

        heap = [(0, 0)]

        visited = set()
        min_cost = 0

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)

            min_cost += dist

            
            for neighbor, edge_dist in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (edge_dist, neighbor))
                    # visited.add(neighbor)

        return min_cost
        