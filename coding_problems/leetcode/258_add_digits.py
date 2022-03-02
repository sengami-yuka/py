class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        s = 0
        while num:
            num, rem = divmod(num, 10)
            s += rem
        return self.addDigits(s)

    def addDigits2(self, num: int) -> int:
        if num <= 9:
            return num
        mod = num % 9
        return 9 if mod == 0 else mod

    def addDigits3(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0


s = Solution()
assert 2 == s.addDigits3(38)
assert 0 == s.addDigits3(0)
assert 9 == s.addDigits3(9)
assert 1 == s.addDigits3(55)
assert 9 == s.addDigits3(18)
