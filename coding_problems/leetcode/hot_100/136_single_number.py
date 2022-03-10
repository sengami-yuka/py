from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans


solution = Solution()
assert 1 == solution.singleNumber([2,2,1])
assert 4 == solution.singleNumber([4,1,2,1,2])
