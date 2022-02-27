from collections import defaultdict


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        odd_c = 0
        for v in d.itervalues():
            if v % 2 == 1:
                odd_c += 1
                if odd_c == 2:
                    return False
        return True

    def canPermutePalindrome2(self, s):
        st = set()
        for c in s:
            if c not in st:
                st.add(c)
            else:
                st.remove(c)
        return len(st) <= 1


s = Solution()
assert s.canPermutePalindrome2('tactcoa')
