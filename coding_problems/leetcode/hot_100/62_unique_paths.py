import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m
        s = m + n - 2
        c = 1
        for i in range(1, m):
            c = c * s // i
            s -= 1
        return c


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, min(m - 1, n - 1))
