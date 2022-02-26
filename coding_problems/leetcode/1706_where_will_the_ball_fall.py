class Solution:
    def findBall(self, grid):
        cols = len(grid[0])
        ans = [-1] * cols
        for j in range(cols):
            col = j
            for row in grid:
                delta = row[col]
                col += delta
                if col < 0 or col == cols or row[col] != delta:
                    break
            else:
                ans[j] = col
        return ans


s = Solution()
assert [1,-1,-1,-1,-1] == s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
assert [-1] == s.findBall([[-1]])
assert [0,1,2,3,4,-1] == s.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])
