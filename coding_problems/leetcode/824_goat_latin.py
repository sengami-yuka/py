VOWEL_SET = set('aeiouAEIOU')


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return ' '.join((word if word[0] in VOWEL_SET else word[1:] + word[0]) + 'ma' + 'a' * i for i, word in enumerate(sentence.split(), 1))


solution = Solution()
ans = solution.toGoatLatin('I speak Goat Latin')
assert ans == 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa', ans

ans = solution.toGoatLatin('The quick brown fox jumped over the lazy dog')
assert ans == 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa', ans
