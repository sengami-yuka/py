import collections


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def f(key):
            ans = s = i = 0
            for j, c in enumerate(answerKey):
                s += c != key
                while s > k:
                    s -= answerKey[i] != key
                    i += 1
                ans = max(ans, j - i + 1)
            return ans

        return max(f('T'), f('F'))


class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = left = cnts_t = cnts_f = 0
        for right, c in enumerate(answerKey):
            cnts_t += c == 'T'
            cnts_f += c == 'F'
            # 当前区间内的t和f的个数不能都大于k，我们只能变k次
            while cnts_t > k and cnts_f > k:
                # 超过最大变动次数了，当前指针的区间最左要向右移动
                cnts_t -= answerKey[left] == 'T'
                cnts_f -= answerKey[left] == 'F'
                left += 1
            ans = max(ans, right - left + 1)
        return ans


class Solution3:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = cnts_t = cnts_f = 0
        for c in answerKey:
            cnts_t += c == 'T'
            cnts_f += c == 'F'
            if cnts_t > k and cnts_f > k:
                cnts_t -= answerKey[left] == 'T'
                cnts_f -= answerKey[left] == 'F'
                left += 1
        return len(answerKey) - left


solution = Solution3()
ans = solution.maxConsecutiveAnswers('TTFF', 2)
assert ans == 4, ans

ans = solution.maxConsecutiveAnswers('TFFT', 1)
assert ans == 3, ans

ans = solution.maxConsecutiveAnswers('TTFTTFTT', 1)
assert ans == 5, ans

ans = solution.maxConsecutiveAnswers('TTFTTFT', 1)
assert ans == 5, ans

ans = solution.maxConsecutiveAnswers('TTFTTFTTT', 1)
assert ans == 6, ans
