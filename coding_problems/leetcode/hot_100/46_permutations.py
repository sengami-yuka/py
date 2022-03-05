from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                ans.append([nums[i]] + p)
        return ans


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


solution = Solution2()
assert sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]) == sorted(solution.permute([1,2,3]))
assert sorted([[0,1],[1,0]]) == sorted(solution.permute([0,1]))
assert [[1]] == solution.permute([1])
