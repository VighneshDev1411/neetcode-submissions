class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and board[nr][nc] == 'O':
                    board[nr][nc] = 'O'
                    dfs(nr, nc)
            

        for r in range(rows):
            for c in range(cols):
                is_edge = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
                if is_edge and board[r][c] == 'O' and (r, c) not in visited:
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'

        





        