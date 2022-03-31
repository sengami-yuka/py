from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        pre = 10000
        for p in prices:
            pre = min(p, pre)
            ans = max(ans, p - pre)
        return ans


solution = Solution()
ans = solution.maxProfit([7,1,5,3,6,4])
assert ans == 5, ans

ans = solution.maxProfit([7,6,4,3,1])
assert ans == 0, ans
