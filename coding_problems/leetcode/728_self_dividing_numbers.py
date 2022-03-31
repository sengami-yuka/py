from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num):
            tmp = num
            while tmp:
                tmp, mod = divmod(tmp, 10)
                if mod == 0 or num % mod != 0:
                    return False
            return True
        return [x for x in range(left, right + 1) if check(x)]
