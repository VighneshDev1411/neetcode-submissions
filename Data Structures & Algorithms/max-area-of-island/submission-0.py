class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        max_area = 0
        area = [0]
        def dfs(r, c):
            visited.add((r, c))
            area[0] += 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    dfs(nr, nc)
                    
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    max_area = max(max_area, area[0])
                    area[0] = 0
                    

        return max_area
                
                


        