class Solution(object):
    def compressString(self, S):
        if not S:
            return ''
        L = len(S)
        ans = []
        target = S[0]
        count = 0
        for c in S:
            if c == target:
                count += 1
            else:
                ans.extend([target, str(count)])
                if len(ans) >= L:
                    return S
                count = 1
                target = c
        ans.extend([target, str(count)])
        if len(ans) >= L:
            return S
        return ''.join(ans)


s = Solution()
assert 'a2b1c5a3' == s.compressString('aabcccccaaa')
assert 'abbccd' == s.compressString('abbccd')
