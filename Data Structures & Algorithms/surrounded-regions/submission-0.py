class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    new_row < 0 or
                    new_row >= len(board) or
                    new_col < 0 or
                    new_col >= len(board[row])
                ):
                    continue

                if board[new_row][new_col] == "X":
                    continue

                if board[new_row][new_col] == "O":
                    board[new_row][new_col] = "#"
                    dfs(new_row, new_col)

        # loop through left column
        for row in range(rows):
            if board[row][0] == "O":
                board[row][0] = "#"
                dfs(row, 0)

        # loop through top row
        for col in range(cols):
            if board[0][col] == "O":
                board[0][col] = "#"
                dfs(0, col)

        # loop through right column
        for row in range(rows):
            if board[row][cols - 1] == "O":
                board[row][cols - 1] = "#"
                dfs(row, cols - 1)

        # loop through bottom row
        for col in range(cols):
            if board[rows - 1][col] == "O":
                board[rows - 1][col] = "#"
                dfs(rows - 1, col)
                            
        # loop through whole grid to fix values
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
            
            
        