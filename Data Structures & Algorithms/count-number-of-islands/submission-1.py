from typing import List

class Solution:
    def finish_def(self, grid: List[List[str]], i: int, j: int, gridtrue: List[List[bool]]) -> bool:
        # Check boundaries
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False

        # Check if water or already visited
        if grid[i][j] == '0' or gridtrue[i][j]:
            return False

        return True

    def dfs(self, grid: List[List[str]], i: int, j: int, gridtrue: List[List[bool]]) -> None:
        gridtrue[i][j] = True

        # Down
        if self.finish_def(grid, i + 1, j, gridtrue):
            self.dfs(grid, i + 1, j, gridtrue)

        # Up
        if self.finish_def(grid, i - 1, j, gridtrue):
            self.dfs(grid, i - 1, j, gridtrue)

        # Right
        if self.finish_def(grid, i, j + 1, gridtrue):
            self.dfs(grid, i, j + 1, gridtrue)

        # Left
        if self.finish_def(grid, i, j - 1, gridtrue):
            self.dfs(grid, i, j - 1, gridtrue)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        gridtrue = [[False] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if self.finish_def(grid, i, j, gridtrue):
                    count += 1
                    self.dfs(grid, i, j, gridtrue)

        return count
