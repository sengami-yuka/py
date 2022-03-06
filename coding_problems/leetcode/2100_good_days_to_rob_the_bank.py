from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return list(range(len(security)))
        N = len(security)
        dec = [0] * N
        inc = [0] * N
        for i in range(1, N):
            if security[i - 1] >= security[i]:
                dec[i] = dec[i - 1] + 1
            if security[-i - 1] <= security[-i]:
                inc[-i - 1] = inc[-i] + 1
        return [i for i in range(time, N - time) if dec[i] >= time and inc[i] >= time]


solution = Solution()
ans = solution.goodDaysToRobBank([5,3,3,3,5,6,2], 2)
assert ans == [2, 3]

ans = solution.goodDaysToRobBank([1,1,1,1,1], 0)
assert ans == [0, 1, 2, 3, 4], ans

ans = solution.goodDaysToRobBank([1,2,3,4,5,6], 2)
assert ans == []

ans = solution.goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8], 2)
assert ans == [5, 10, 14]

