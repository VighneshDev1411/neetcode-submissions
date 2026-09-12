class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        fresh_count = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        max_time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
                
        while queue:
            r, c, time = queue.popleft()
            visited.add((r, c))
            max_time = max(max_time, time)
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))
        
        return max_time if fresh_count == 0 else -1
                    








        