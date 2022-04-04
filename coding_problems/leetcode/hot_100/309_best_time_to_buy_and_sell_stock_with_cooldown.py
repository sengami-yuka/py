from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0], dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]), max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp0, dp1, dpc0 = 0, -prices[0], 0
        for i in range(1, n):
            dp0, dp1, dpc0 = max(dp0, dp1 + prices[i]), max(dp1, dpc0 - prices[i]), dp0
        return dp0


solution = Solution2()
ans = solution.maxProfit([1,2,3,0,2])
assert ans == 3, ans

ans = solution.maxProfit([1])
assert ans == 0, ans
