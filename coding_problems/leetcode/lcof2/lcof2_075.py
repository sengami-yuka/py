from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = max(arr1)
        size = m + 1
        f = [0] * size
        for i in arr1:
            f[i] += 1
        ans = []
        for i in arr2:
            if f[i] > 0:
                ans.extend([i] * f[i])
                f[i] = 0
        for i in range(size):
            if f[i]:
                ans.extend([i] * f[i])
        return ans


solution = Solution()
assert [2,2,2,1,4,3,3,9,6,7,19] == solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])
