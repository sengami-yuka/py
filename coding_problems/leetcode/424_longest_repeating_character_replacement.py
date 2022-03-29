from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxc = left = 0
        for right, c in enumerate(s):
            d[c] += 1
            maxc = max(maxc, d[c])
            if right - left + 1 - maxc > k:
                d[s[left]] -= 1
                left += 1
        return len(s) - left
