class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isSafe(board, row, col):
            r, c = row, col

            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False 

                r -= 1
                c -= 1

            r, c = row, col

            while r >= 0:
                if board[r][c] == 'Q':
                    return False
                
                r -= 1

            r, c = row, col

            while r >= 0 and c < len(board[0]):
                if board[r][c] == 'Q':
                    return False 

                r -= 1
                c += 1

            return True


        
        def backtrack(ind, board):
            if ind == len(board):
                ans.append([''.join(r) for r in board])
                return 

            for c in range(len(board[0])):
                if isSafe(board, ind, c):
                    board[ind][c] = 'Q'
                    backtrack(ind + 1, board)
                    board[ind][c] = '.'  

        backtrack(0, board)
        return ans 


        