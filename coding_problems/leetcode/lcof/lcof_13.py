class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def check(row, col):
            a = 0
            while row:
                a += row % 10
                row //= 10
            while col:
                a += col % 10
                col //= 10
            return a <= k

        visited = set([(0, 0)])
        st = [(0, 0)]
        while st:
            i, j = st.pop()
            if i < m - 1 and (i + 1, j) not in visited and check(i + 1, j):
                visited.add((i + 1, j))
                st.append((i + 1, j))
            if j < n - 1 and (i, j + 1) not in visited and check(i, j + 1):
                visited.add((i, j + 1))
                st.append((i, j + 1))
        return len(visited)


def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)


solution = Solution2()
ans = solution.movingCount(2, 3, 1)
assert ans == 3, ans

ans = solution.movingCount(3, 1, 0)
assert ans == 1, ans

ans = solution.movingCount(3, 2, 17)
assert ans == 6, ans
