import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m
        s = m + n - 2
        c = 1
        for i in range(1, m):
            c *= s / i
            s -= 1
        return int(round(c))
        # return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))
