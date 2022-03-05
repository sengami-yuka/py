from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(int.bit_count(i))
        print(ans)
        return ans


class Solution2:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        target = 1
        step = 1
        for i in range(1, n + 1):
            a = ans[i - step] + 1
            ans.append(a)
            if a == target:
                target += 1
                step *= 2
        return ans


solution = Solution2()
assert [0,1,1] == solution.countBits(2)
assert [0,1,1,2,1,2] == solution.countBits(5)
