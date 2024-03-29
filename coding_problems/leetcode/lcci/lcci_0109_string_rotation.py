class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and (s2 * 2).find(s1) >= 0


s = Solution()
assert s.isFlipedString('waterbottle', 'erbottlewat')
assert not s.isFlipedString('aa', 'aba')
