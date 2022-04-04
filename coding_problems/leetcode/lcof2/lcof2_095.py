import pprint


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        dp = [0] * n
        if text1[0] == text2[0]:
            dp[0] = 1
        for j in range(1, n):
            dp[j] = dp[j - 1] or int(text1[0] == text2[j])
        for i in range(1, m):
            pre = dp[0] = dp[0] or int(text1[i] == text2[0])
            for j in range(1, n):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = tmp
        return dp[-1]


solution = Solution()
ans = solution.longestCommonSubsequence('abcde', 'ace')
assert ans == 3, ans

ans = solution.longestCommonSubsequence('abc', 'abc')
assert ans == 3, ans

ans = solution.longestCommonSubsequence('abc', 'def')
assert ans == 0, ans

ans = solution.longestCommonSubsequence('bl', 'yby')
assert ans == 1, ans

ans = solution.longestCommonSubsequence('bsbininm', 'jmjkbkjkv')
assert ans == 1, ans

ans = solution.longestCommonSubsequence('papmretkborsrurgtina', 'nsnupotstmnkfcfavaxgl')
assert ans == 6, ans
