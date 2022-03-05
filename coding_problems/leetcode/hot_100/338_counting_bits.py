from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        step = 1
        target = 1
        for i in range(1, n + 1):
            a = ans[i - step] + 1
            if a == target:
                target += 1
                step *= 2
            ans.append(a)
        return ans
