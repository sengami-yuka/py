import math


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        def multiply(a, b):
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j])
            return c

        def matrix_pow(a, n):
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n)
        return res[0][0]


class Solution3:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(round(fibn / sqrt5))


solution = Solution()
assert 2 == solution.climbStairs(2)
assert 3 == solution.climbStairs(3)
assert 5 == solution.climbStairs(4)
assert 8 == solution.climbStairs(5)
