class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for element in matrix:
            left = 0
            right = len(matrix[0]) - 1
            while left <= right:
                mid = (left + right) // 2
                if element[mid] == target:
                    return True

                if element[mid] < target:
                    left += 1

                if element[mid] > target:
                    right -= 1

        return False

                
                    
            