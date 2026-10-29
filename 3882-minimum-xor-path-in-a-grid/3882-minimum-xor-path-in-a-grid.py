from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        limit = 1
        for row in grid:
            limit = max(limit, max(row) + 1)
        limit = 1 << (limit - 1).bit_length()

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = {val}
                else:
                    prev = set()
                    if i > 0:
                        prev |= dp[j]
                    if j > 0:
                        prev |= dp[j - 1]
                    dp[j] = {x ^ val for x in prev}

        return min(dp[-1])