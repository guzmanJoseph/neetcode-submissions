class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(row, col):
            if (row >= len(grid) or
            col >= len(grid[row]) or
            row < 0 or
            col < 0 or
            grid[row][col] == 0 or
            (row, col) in visited):
                return 0

            area = 1
            visited.add((row, col))
            area += dfs(row + 1, col)
            area += dfs(row, col + 1)
            area += dfs(row - 1, col)
            area += dfs(row, col - 1)
            return area
            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                area = dfs(row, col)
                if max_area < area:
                    max_area = area
        return max_area
            
            

        