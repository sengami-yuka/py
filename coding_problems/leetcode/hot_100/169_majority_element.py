from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        target = len(nums) // 2
        for i in nums:
            d[i] += 1
            if d[i] > target:
                return i


class Solution2:  # Boyer-Moore
    def majorityElement(self, nums: List[int]) -> int:
        c = None
        v = 0
        for i in nums:
            if v == 0:
                c = i
            if i == c:
                v += 1
            else:
                v -= 1
        return c


solution = Solution2()
assert 3 == solution.majorityElement([3,2,3])
assert 2 == solution.majorityElement([2,2,1,1,1,2,2])
