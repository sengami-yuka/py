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


solution = Solution()
ans = solution.maxConsecutiveAnswers('TTFF', 2)
assert ans == 4, ans

ans = solution.maxConsecutiveAnswers('TFFT', 1)
assert ans == 3, ans

ans = solution.maxConsecutiveAnswers('TTFTTFTT', 1)
assert ans == 5, ans

ans = solution.maxConsecutiveAnswers('TTFTTFTTT', 1)
assert ans == 6, ans
