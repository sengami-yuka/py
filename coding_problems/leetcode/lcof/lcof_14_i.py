import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1, 2, 4, 6, 9] + [0] * (n - 6)
        for i in range(5, n - 1):
            dp[i] = dp[i - 3] * 3
        return dp[n - 2]


d = {
    2: 1,
    3: 2,
    4: 4,
    5: 6,
    6: 9
}


class Solution2:
    def cuttingRope(self, n: int) -> int:
        if n in d:
            return d[n]
        dp1, dp2, dp3 = 4, 6, 9
        for _ in range(n - 6):
            dp1, dp2, dp3 = dp2, dp3, dp1 * 3
        return dp3


class Solution3:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        ans = 1
        while n > 4:
            n -= 3
            ans *= 3
        ans *= n
        return ans


class Solution4:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = divmod(n, 3)
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


solution = Solution3()
ans = solution.cuttingRope(2)
assert ans == 1, ans

ans = solution.cuttingRope(10)
assert ans == 36, ans
