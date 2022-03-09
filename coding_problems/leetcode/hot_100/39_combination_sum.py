from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, val):
            if val == target:
                ans.append(a[:])
                return 1
            elif val > target:
                return 1
            for i in range(start, L):
                a.append(candidates[i])
                need_break = dfs(i, val + candidates[i])
                a.pop()
                if need_break:
                    break
            return 0

        candidates.sort()
        ans = []
        a = []
        L = len(candidates)
        dfs(0, 0)
        return ans


solution = Solution()
ans = solution.combinationSum([2,3,6,7], 7)
assert [[2, 2, 3], [7]] == ans
ans = solution.combinationSum([2,3,5], 8)
assert [[2, 2, 2, 2], [2, 3, 3], [3, 5]] == ans
