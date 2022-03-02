class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        right = numRows - 1
        i = 0
        for c in s:
            rows[i] += c
            if i == 0:
                delta = 1
            elif i == right:
                delta = -1
            i += delta
        return ''.join(rows)


s = Solution()
assert 'PAHNAPLSIIGYIR' == s.convert('PAYPALISHIRING', 3)
assert 'PINALSIGYAHRPI' == s.convert('PAYPALISHIRING', 4)
assert 'A' == s.convert('A', 1)
assert 'ABC' == s.convert('ABC', 1)
