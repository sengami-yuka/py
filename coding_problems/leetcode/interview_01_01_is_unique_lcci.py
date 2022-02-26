class Solution:
    def isUnique(self, astr):  # hash
        s = set()
        for c in astr:
            if c in s:
                return False
            s.add(c)
        return True

    def isUnique2(self, astr):  # bitwise
        b = 0
        for c in astr:
            iv = ord(c)
            if b >> iv & 1:
                return False
            b |= 1 << iv
        return True

    def isUnique3(self, astr):  # sort
        s = sorted(astr)
        for i in range(1, len(astr)):
            if s[i - 1] == s[i]:
                return False
        return True


s = Solution()
print s.isUnique2("abc")
