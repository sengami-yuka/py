from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i, v in enumerate(nums):
            right -= v
            if left == right:
                return i
            left += v
        return -1


solution = Solution()
assert 3 == solution.pivotIndex([1,7,3,6,5,6])
assert -1 == solution.pivotIndex([1, 2, 3])
assert 0 == solution.pivotIndex([2, 1, -1])
