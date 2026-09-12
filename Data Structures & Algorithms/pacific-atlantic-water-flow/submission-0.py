class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return None 

        rows = len(heights)
        cols = len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()


        def bfs(starts, visited):
            queue = deque(starts)
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for cell in starts:
                visited.add(cell)

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            queue.append((nr, nc))
                            visited.add((nr, nc))

        
        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)] 
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        bfs(pacific_starts, pacific_visited)
        bfs(atlantic_starts, atlantic_visited)

        result = list(pacific_visited & atlantic_visited)

        return [[r, c] for r, c in result]


            



        