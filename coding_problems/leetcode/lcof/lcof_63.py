from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        ans = 0
        for price in prices:
            if price < minp:
                minp = price
            else:
                ans = max(ans, price - minp)
        return ans
