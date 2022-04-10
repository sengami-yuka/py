
class Solution:
    def translateNum(self, num: int) -> int:
        pre = 0
        dp = [1]
        while num:
            num, mod = divmod(num, 10)
            if len(dp) > 1 and mod and mod * 10 + pre <= 25:
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])
            pre = mod
        return dp[-1]


class Solution2:
    def translateNum(self, num: int) -> int:
        pre = 0
        dp1 = 1
        dp2 = 0
        while num:
            num, mod = divmod(num, 10)
            if mod and mod * 10 + pre <= 25:
                dp1, dp2 = dp1 + dp2, dp1
            else:
                dp2 = dp1
            pre = mod
        return dp1


solution = Solution()

ans = solution.translateNum(0)
assert ans == 1, ans

ans = solution.translateNum(12258)
assert ans == 5, ans

ans = solution.translateNum(312258)
assert ans == 5, ans

ans = solution.translateNum(10312258)
assert ans == 10, ans

ans = solution.translateNum(11)
assert ans == 2, ans

