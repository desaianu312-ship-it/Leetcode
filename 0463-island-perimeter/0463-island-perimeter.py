class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        land = 0
        neighbors = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    land += 1

                    if r + 1 < rows and grid[r+1][c] == 1:
                        neighbors += 1

                    if c + 1 < cols and grid[r][c+1] == 1:
                        neighbors += 1

        return land * 4 - neighbors * 2
        