from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            c = i
            subset = []
            idx = 0
            while c:
                if c & 1:
                    subset.append(nums[idx])
                c >>= 1
                idx += 1
            ans.append(subset)
        return ans


solution = Solution()
assert [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] == solution.subsets([1,2,3])
assert [[],[0]] == solution.subsets([0])
