from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = ['(']

        def helper(left, right):
            if left == n:
                ans.append(''.join(s + [')'] * (2 * n - len(s))))
                return
            if left < n:
                s.append('(')
                helper(left + 1, right)
                s.pop()
            if left > right:
                s.append(')')
                helper(left, right + 1)
                s.pop()
        helper(1, 0)
        return ans


solution = Solution()
ans = solution.generateParenthesis(1)
print(ans)

ans = solution.generateParenthesis(2)
print(ans)

ans = solution.generateParenthesis(3)
print(ans)
