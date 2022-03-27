from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        n_sum = mean * (n + len(rolls)) - sum(rolls)
        if n <= n_sum <= 6 * n:
            q, m = divmod(n_sum, n)
            return [q + 1] * m + [q] * (n - m)
        return []


solution = Solution()
ans = solution.missingRolls([3,2,4,3], 4, 2)
print(ans)

ans = solution.missingRolls([1,5,6], 3, 4)
print(ans)

ans = solution.missingRolls([1,2,3,4], 6, 4)
print(ans)

ans = solution.missingRolls([1], 3, 1)
print(ans)
