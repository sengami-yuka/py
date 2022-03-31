from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
            triangle[i][-1] += triangle[i - 1][-1]
        return min(triangle[-1])


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)


solution = Solution()
ans = solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
assert ans == 11, ans

ans = solution.minimumTotal([[-10]])
assert ans == -10, ans
