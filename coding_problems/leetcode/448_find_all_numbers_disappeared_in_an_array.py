from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(range(1, len(nums) + 1))
        for i in nums:
            s.discard(i)
        return list(s)


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = num % n
            nums[x - 1] += n
        return [i + 1 for i, v in enumerate(nums) if v <= n]


solution = Solution2()
assert [5,6] == solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
assert [2] == solution.findDisappearedNumbers([1,1])
