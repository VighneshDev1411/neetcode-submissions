class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid)
        max_height = max(max(row) for row in grid)

        def canVisit(t):      
            visited = {(0, 0)}
            queue = deque([(0 ,0)])
            if grid[0][0] > t:
                return False 
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if grid[nr][nc] <= t:
                            queue.append((nr, nc))
                            visited.add((nr, nc))

            return False 
        
        for t in range(max_height + 1):
            if canVisit(t):
                return t

        return max_height

            



    

        
 

        