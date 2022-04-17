from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(x):
            ans.append(x)
            for i in range(10):
                y = 10 * x + i
                if y <= n:
                    dfs(y)
                else:
                    break
        ans = []
        for i in range(1, min(n + 1, 10)):
            dfs(i)
        return ans


class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(1, min(n + 1, 10)):
            st = [i]
            while st:
                x = st.pop()
                ans.append(x)
                for j in reversed(range(10)):
                    y = 10 * x + j
                    if y <= n:
                        st.append(y)
        return ans


class Solution3:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans


class Solution4:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)


solution = Solution4()
ans = solution.lexicalOrder(13)
assert ans == [1,10,11,12,13,2,3,4,5,6,7,8,9], ans

ans = solution.lexicalOrder(2)
assert ans == [1,2], ans

ans = solution.lexicalOrder(123)
# print(ans)

# ans = solution.lexicalOrder(1234)
# print(ans)
