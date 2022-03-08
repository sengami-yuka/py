from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[:2]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)


solution = Solution()
assert 15 == solution.minCostClimbingStairs([10, 15, 20])
assert 6 == solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
