class Solution(object):
    def oneEditAway(self, first, second):
        if abs(len(first) - len(second)) > 1:
            return False
        if len(first) < len(second):
            first, second = second, first
        for i in range(len(second)):
            if first[i] != second[i]:
                return first[i + 1:] == second[i:] or first[i + 1:] == second[i + 1:]
        return True


s = Solution()
assert s.oneEditAway('pale', 'ple')
assert not s.oneEditAway('pales', 'pal')
assert s.oneEditAway('pales', 'paled')
