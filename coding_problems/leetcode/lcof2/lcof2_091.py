from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])


class Solution2:
    def minCost(self, costs: List[List[int]]) -> int:
        toRED = toBLUE = toGREEN = 0
        for cost in costs:
            toRED, toBLUE, toGREEN = cost[0] + min(toBLUE, toGREEN), cost[1] + min(toRED, toGREEN), cost[2] + min(toRED, toBLUE)
        return min(toRED, toBLUE, toGREEN)


solution = Solution2()
ans = solution.minCost([[17,2,17],[16,16,5],[14,3,19]])
assert ans == 10, ans

ans = solution.minCost([[7,6,2]])
assert ans == 2, ans
