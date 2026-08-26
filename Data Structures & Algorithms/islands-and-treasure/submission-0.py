from collections import deque
INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col

                if (new_row >= len(grid) or
                    new_col >= len(grid[new_row]) or
                    new_row < 0 or
                    new_col < 0
                    ):
                        continue

                if grid[new_row][new_col] != INF:
                    continue
                grid[new_row][new_col] = grid[row][col] + 1
                queue.append((new_row, new_col))


        