class Solution(object):
    def reverse(self, x):
        rev = 0
        MAX = 214748364
        if x < 0:
            x = -x
            neg = True
        else:
            neg = False
        while x:
            rem = x % 10
            if rev > MAX:
                return 0
            x /= 10
            rev = rev * 10 + rem
        if neg:
            return -rev
        return rev


s = Solution()
assert 321 == s.reverse(123)
assert -321 == s.reverse(-123)
assert 21 == s.reverse(120)
