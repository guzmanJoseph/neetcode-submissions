class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(row, col, visited):
            visited.add((row, col))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    new_row < 0 or
                    new_row >= rows or
                    new_col < 0 or
                    new_col >= cols
                ):
                    continue

                if (new_row, new_col) in visited:
                    continue

                if heights[new_row][new_col] < heights[row][col]:
                    continue
                
                dfs(new_row, new_col, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result
        