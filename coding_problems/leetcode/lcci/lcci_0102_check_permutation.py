from collections import defaultdict


class Solution:
    def CheckPermutation(self, s1, s2):
        return sorted(s1) == sorted(s2)

    def CheckPermutation2(self, s1, s2):
        d = defaultdict(int)
        for c in s1:
            d[c] += 1
        for c in s2:
            d[c] -= 1
        return all(x == 0 for x in d.values())
