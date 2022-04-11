from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, chars = 1, 0
        for c in s:
            w = widths[ord(c) - 97]
            chars += w
            if chars > 100:
                lines += 1
                chars = w
        return [lines, chars]
