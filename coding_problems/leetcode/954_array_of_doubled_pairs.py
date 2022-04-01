from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True


solution = Solution()
assert not solution.canReorderDoubled([3,1,3,6])

assert not solution.canReorderDoubled([2,1,2,6])

assert solution.canReorderDoubled([4,-2,2,-4])

assert solution.canReorderDoubled([-6,-3])
