class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hash_set = set()
        path = []

        def backtrack(row, col, i):

            if i == len(word):
                return True
            if (row < 0 or
                row >= len(board) or
                col < 0 or
                col >= len(board[row]) or
                (row, col) in hash_set
            ):
                return False

            if board[row][col] != word[i]:
                return False

            hash_set.add((row, col)) 

            found = (
                backtrack(row - 1, col, i + 1) or
                backtrack(row + 1, col, i + 1) or
                backtrack(row, col - 1, i + 1) or
                backtrack(row, col + 1, i + 1)
            )

            hash_set.remove((row, col))

            return found

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(row, col, 0):
                    return True

        return False

            
        