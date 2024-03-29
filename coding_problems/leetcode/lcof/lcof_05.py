class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


class Solution2:
    def replaceSpace(self, s: str) -> str:
        ans = []
        for c in s:
            if c == ' ':
                ans.append('%20')
            else:
                ans.append(c)
        return ''.join(ans)
