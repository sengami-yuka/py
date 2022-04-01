import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            tmp = float('inf')
            for j in range(1, int(math.sqrt(i)) + 1):
                tmp = min(tmp, dp[i - j * j])
            dp[i] = 1 + tmp
        return dp[-1]


class Solution2:
    def numSquares(self, n: int) -> int:
        def isSqure(x):
            y = int(math.sqrt(x))
            return y * y == x

        def check4(x):
            while x % 4 == 0:
                x //= 4
            return x % 8 == 7

        if isSqure(n):
            return 1
        if check4(n):
            return 4
        for i in range(1, int(math.sqrt(n)) + 1):
            j = n - i * i
            if isSqure(j):
                return 2
        return 3


solution = Solution2()
ans = solution.numSquares(12)
assert ans == 3, ans

ans = solution.numSquares(13)
assert ans == 2, ans
