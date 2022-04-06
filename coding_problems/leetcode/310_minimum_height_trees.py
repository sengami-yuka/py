from typing import List
from collections import defaultdict, deque


class Solution:  # brute force bfs
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        e = defaultdict(list)
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        ans = []
        minh = float('inf')
        for v in range(n):
            q = deque([v])
            h = 0
            visited = {v}
            while q:
                h += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    for child in e[node]:
                        if child not in visited:
                            q.append(child)
                            visited.add(child)
            if h < minh:
                minh = h
                ans = [v]
            elif h == minh:
                ans.append(v)
        return ans


class Solution2:  # outside bfs
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        e = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
            deg[u] += 1
            deg[v] += 1
        q = deque()
        for i, v in enumerate(deg):
            if v == 1:
                q.append(i)
        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)
                for child in e[node]:
                    deg[child] -= 1
                    if deg[child] == 1:
                        q.append(child)
        return res


class Solution3:  # topsort
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q


class Solution4:  # math + bfs
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


class Solution5:  # math + dfs
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n
        maxDepth, node = 0, -1

        def dfs(x: int, pa: int, depth: int):
            nonlocal maxDepth, node
            if depth > maxDepth:
                maxDepth, node = depth, x
            parents[x] = pa
            for y in g[x]:
                if y != pa:
                    dfs(y, x, depth + 1)
        dfs(0, -1, 1)
        maxDepth = 0
        dfs(node, -1, 1)

        path = []
        while node != -1:
            path.append(node)
            node = parents[node]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


solution = Solution2()
ans = solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
assert ans == [1], ans

ans = solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
assert ans == [3,4], ans

ans = solution.findMinHeightTrees(1, [])
assert ans == [0], ans

ans = solution.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
assert ans == [3], ans
