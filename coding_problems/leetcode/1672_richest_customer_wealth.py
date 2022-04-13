from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for row in accounts:
            ans = max(ans, sum(row))
        return ans


class Solution2:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
