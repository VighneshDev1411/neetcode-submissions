class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c, ind):
            if board[r][c] != word[ind]:
                return False 

            if ind == len(word) - 1:
                return True
            

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, ind + 1):
                            return True

            visited.remove((r, c))
            return False

            

        for r in range(rows):
            for c in range(cols):
                # if (r, c) not in visited:
                    if dfs(r, c, 0):
                        return True


        return False 
        