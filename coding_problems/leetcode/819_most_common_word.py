import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        s = ''
        ct = Counter()
        for c in paragraph:
            if c.isalpha():
                s += c.lower()
            elif s:
                if s not in banned:
                    ct[s] += 1
                s = ''
        if s and s not in banned:
            ct[s] += 1
        return ct.most_common(1)[0][0]


class Solution2:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter(w for w in re.findall(r'\w+', paragraph.lower()) if w not in set(banned)).most_common(1)[0][0]


solution = Solution()
ans = solution.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'])
assert ans == 'ball', ans

ans = solution.mostCommonWord('Bob. hIt, baLl', ['bob', 'hit'])
assert ans == 'ball', ans
