class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


solution = Solution()
assert 'cdefgab' == solution.reverseLeftWords('abcdefg', 2)
assert 'umghlrlose' == solution.reverseLeftWords('lrloseumgh', 6)
