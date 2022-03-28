class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        while n:
            n >>= 1
            if n & 1 == last:
                return False
            last = n & 1
        return True


class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ n >> 1
        return x & x + 1 == 0
