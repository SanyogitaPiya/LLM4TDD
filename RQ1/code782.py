class Solution:
    def movesToChessboard(self, board):
        n = len(board)
        
        row_sum = sum(board[i][0] == i % 2 for i in range(n))
        col_sum = sum(board[0][i] == i % 2 for i in range(n))
        
        row_diff = col_diff = 0
        for i in range(n):
            for j in range(n):
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) == 1:
                    return -1
                
        for i in range(n):
            row_diff += board[i][0] != i % 2
            col_diff += board[0][i] != i % 2
        
        if n % 2 == 0:
            row_diff = min(row_diff, n - row_diff)
            col_diff = min(col_diff, n - col_diff)
        else:
            # In case of odd n, either row_diff or col_diff must be even
            if row_diff % 2 == 1:
                row_diff = n - row_diff
            if col_diff % 2 == 1:
                col_diff = n - col_diff
            row_diff = row_diff // 2
            col_diff = col_diff // 2
        
        return (row_diff + col_diff) // 2