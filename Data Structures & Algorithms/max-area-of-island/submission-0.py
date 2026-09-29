from typing import List

class Solution:
    def finish_def(self, grid: List[List[str]], i: int, j: int) -> bool:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False

  
        if grid[i][j] == 0:
            return False

        return True

    def dfs(self, grid: List[List[str]], i: int, j: int,count:int) -> int:
        grid[i][j] = 0
        count+=1 
        # Down
        if self.finish_def(grid, i + 1, j):
            count=self.dfs(grid, i + 1, j,count)

        # Up
        if self.finish_def(grid, i - 1, j):
            count=self.dfs(grid, i - 1, j,count)

        # Right
        if self.finish_def(grid, i, j + 1):
            count=self.dfs(grid, i, j + 1,count)

        # Left
        if self.finish_def(grid, i, j - 1):
            count=self.dfs(grid, i, j - 1,count)

        return count

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        count = 0
        maxcount=0
        for i in range(rows):
            for j in range(cols):
                if self.finish_def(grid, i, j): 
                    count = self.dfs(grid, i, j,count)
                    maxcount=max(maxcount,count)
                    count=0

        return maxcount
