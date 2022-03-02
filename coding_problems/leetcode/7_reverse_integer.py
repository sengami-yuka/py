class Solution:
    def reverse(self, x):
        rev = 0
        MIN = -214748364
        if x > 0:
            x = -x
            pos = True
        else:
            pos = False
        while x:
            if rev < MIN:
                return 0
            rem = x % 10
            if rem > 0:
                rem -= 10
            x = (x - rem) / 10
            rev = rev * 10 + rem
        if pos:
            return -rev
        return rev


s = Solution()
assert 321 == s.reverse(123)
assert -321 == s.reverse(-123)
assert 21 == s.reverse(120)
