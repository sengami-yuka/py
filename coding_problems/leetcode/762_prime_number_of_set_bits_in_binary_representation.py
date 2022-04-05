primes = {2,3,5,7,11,13,17,19}


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(i.bit_count() in primes for i in range(left, right + 1))


class Solution2:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(((1 << x.bit_count()) & 665772) != 0 for x in range(left, right + 1))


solution = Solution2()
ans = solution.countPrimeSetBits(6, 10)
assert ans == 4, ans

ans = solution.countPrimeSetBits(10, 15)
assert ans == 5, ans
