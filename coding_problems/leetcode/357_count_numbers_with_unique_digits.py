import math


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = 1
        for i in range(n):
            dp += 9 * math.perm(9, i)
        return dp


class Solution2:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res


solution = Solution()
ans = solution.countNumbersWithUniqueDigits(2)
assert ans == 91, ans

ans = solution.countNumbersWithUniqueDigits(0)
assert ans == 1, ans
