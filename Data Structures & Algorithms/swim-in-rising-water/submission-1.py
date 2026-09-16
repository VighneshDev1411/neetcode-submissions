""" Most Optimal """

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while pq:
            cost, r, c = heapq.heappop(pq)

            # if (r, c) in visited:
            #     continue 
            
            if (r, c) == (rows - 1, cols - 1):
                return cost

            for dr, dc in directions:
                nr, nc = dr + r, dc + c 
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_cost = max(cost, grid[nr][nc])
                    heapq.heappush(pq, (new_cost, nr ,nc))

        return -1


