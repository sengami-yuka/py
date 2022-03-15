from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def dfs(i, val):
            nonlocal ans, target
            if i == n:
                if val > target:
                    target = val
                    ans = 1
                elif val == target:
                    ans += 1
                return
            dfs(i + 1, val)
            dfs(i + 1, val | nums[i])
        target = 0
        n = len(nums)
        ans = 0
        dfs(0, 0)
        return ans


solution = Solution()
assert 2 == solution.countMaxOrSubsets([3,1])
assert 7 == solution.countMaxOrSubsets([2,2,2])
assert 6 == solution.countMaxOrSubsets([3,2,1,5])
