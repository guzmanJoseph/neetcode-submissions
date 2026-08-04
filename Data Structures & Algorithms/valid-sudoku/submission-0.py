class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # loop to check for rows
        for i in range(9):
            setRow = set()
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                if value in setRow:
                    return False
                
                setRow.add(value)

        # loop to check columns
        for i in range(9):
            setCol = set()
            for j in range(9):
                value = board[j][i]

                if value == ".":
                    continue

                if value in setCol:
                    return False
                
                setCol.add(value)

        # loop to check boxes
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                setBox = set()

                for i in range(3):
                    for j in range(3):
                        value = board[boxRow + i][boxCol + j]

                        if value == ".":
                            continue

                        if value in setBox:
                            return False

                        setBox.add(value)
        return True