from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


solution = Solution()
ans = solution.maxValue([[1,2,5],[3,2,1]])
assert ans == 9, ans
