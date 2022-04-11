from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = len(nums)
        for i in reversed(range(ans)):
            if nums[i] == val:
                ans -= 1
                nums[i], nums[ans] = nums[ans], nums[i]
        return ans


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i


solution = Solution2()
nums = [3,2,2,3]
ans = solution.removeElement(nums, 3)
print(nums[:ans])

nums = [0,1,2,2,3,0,4,2]
ans = solution.removeElement(nums, 2)
print(nums[:ans])
