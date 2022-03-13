class Solution:
    def replaceSpaces(self, S, length):
        return S[:length].replace(' ', '%20')


s = Solution()
assert 'Mr%20John%20Smith' == s.replaceSpaces('Mr John Smith ', 13)
assert '%20%20%20%20%20' == s.replaceSpaces('               ', 5)
