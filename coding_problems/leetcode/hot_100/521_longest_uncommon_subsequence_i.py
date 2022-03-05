class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


solution = Solution()
assert 3 == solution.findLUSlength('aba', 'cdc')
assert 3 == solution.findLUSlength('aaa', 'bbb')
assert -1 == solution.findLUSlength('aaa', 'aaa')
