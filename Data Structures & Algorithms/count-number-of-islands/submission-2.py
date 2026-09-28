from typing import List

class Solution:
    def finish_def(self, grid: List[List[str]], i: int, j: int) -> bool:
        # Check boundaries
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False

        # Check if water or already visited
        if grid[i][j] == '0':
            return False

        return True

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        grid[i][j] = '0'

        # Down
        if self.finish_def(grid, i + 1, j):
            self.dfs(grid, i + 1, j)

        # Up
        if self.finish_def(grid, i - 1, j):
            self.dfs(grid, i - 1, j)

        # Right
        if self.finish_def(grid, i, j + 1):
            self.dfs(grid, i, j + 1)

        # Left
        if self.finish_def(grid, i, j - 1):
            self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        for i in range(rows):
            for j in range(cols):
                if self.finish_def(grid, i, j):
                    count += 1
                    self.dfs(grid, i, j)

        return count
