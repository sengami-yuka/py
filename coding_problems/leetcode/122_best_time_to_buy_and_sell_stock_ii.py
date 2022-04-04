from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0, dp1 = 0, -prices[0]
        for i in range(1, len(prices)):
            dp0, dp1 = max(dp0, dp1 + prices[i]), max(dp1, dp0 - prices[i])
        return dp0


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        last = len(prices) - 1
        for i, v in enumerate(prices):
            if i < last:
                diff = prices[i + 1] - v
                if diff > 0:
                    ans += diff
        return ans


solution = Solution()
ans = solution.maxProfit([7,1,5,3,6,4])
assert ans == 7, ans

ans = solution.maxProfit([1,2,3,4,5])
assert ans == 4, ans

ans = solution.maxProfit([7,6,4,3,1])
assert ans == 0, ans
