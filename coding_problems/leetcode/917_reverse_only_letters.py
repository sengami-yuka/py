class Solution:
    def reverseOnlyLetters(self, s):
        i = 0
        j = len(s) - 1
        res = list(s)
        while 1:
            while i < j and not s[i].isalpha():
                i += 1
            while j > i and not s[j].isalpha():
                j -= 1
            if i >= j:
                break
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return ''.join(res)

    def reverseOnlyLetters2(self, s):
        letters = [x for x in s if x.isalpha()]
        return ''.join([s[i] if not s[i].isalpha() else letters.pop() for i in range(len(s))])


s = Solution()

assert 'dc-ba' == s.reverseOnlyLetters('ab-cd')
assert 'j-Ih-gfE-dCba' == s.reverseOnlyLetters('a-bC-dEf-ghIj')
assert 'Qedo1ct-eeLg=ntse-T!' == s.reverseOnlyLetters('Test1ng-Leet=code-Q!')
assert '1234' == s.reverseOnlyLetters('1234')
