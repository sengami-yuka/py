class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return int.bit_count(x ^ y)

    def hammingDistance2(self, x: int, y: int) -> int:
        s = x ^ y
        d = 0
        while s:
            d += s & 1
            s >>= 1
        return d

    def hammingDistance3(self, x: int, y: int) -> int:
        s = x ^ y
        d = 0
        while s:
            s &= s - 1
            d += 1
        return d


solution = Solution()
assert 2 == solution.hammingDistance(1, 4)
assert 1 == solution.hammingDistance(3, 1)
assert 2 == solution.hammingDistance2(1, 4)
assert 1 == solution.hammingDistance2(3, 1)
assert 2 == solution.hammingDistance3(1, 4)
assert 1 == solution.hammingDistance3(3, 1)
