class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}

        def dfs(r, c):
            largest = 1

            if (r, c) in dp:
                    return dp[(r, c)]

            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r][c]:
                        largest = max(largest, 1 + dfs(nr, nc))

            dp[(r, c)] = largest

            return largest

        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))


        return answer

            
            


        