class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        ans = len(s)
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if check(i, j):
                    ans += 1
        return ans


class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        ans = n
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if s[i] == s[j] and (i + 1 >= j - 1 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    ans += 1
        return ans


class Solution3:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, i + 2):
                left = i
                right = j
                while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                    ans += 1
        return ans


class Solution4:  # Manacher
    def countSubstrings(self, s: str) -> int:
        t = '$#' + '#'.join(s) + '#!'
        n = len(t) - 1
        iMax = rMax = ans = 0
        f = [0] * n
        for i in range(1, n):
            f[i] = min(rMax - i + 1, f[2 * iMax - i]) if i <= rMax else 1
            while t[i + f[i]] == t[i - f[i]]:
                f[i] += 1
            if i + f[i] - 1 > rMax:
                iMax = i
                rMax = i + f[i] - 1
            ans += f[i] // 2
        return ans


solution = Solution4()
ans = solution.countSubstrings('abc')
assert 3 == ans, ans

ans = solution.countSubstrings('aaa')
assert 6 == ans, ans

ans = solution.countSubstrings('aaaaa')
assert 15 == ans, ans
