import collections
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        ans = 3
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)

        visited = [False] * n
        q = collections.deque([0])
        visited[0] = True
        d = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for child in g[node]:
                    if not visited[child]:
                        q.append(child)
                        visited[child] = True
                        p = patience[child]
                        tmp = 2 * d
                        if tmp > p:
                            tmp += p * ((tmp - 1) // p)
                        tmp += 1
                        if tmp > ans:
                            ans = tmp
            d += 1
        return ans


solution = Solution()
ans = solution.networkBecomesIdle([[0,1],[1,2]], [0,2,1])
assert ans == 8, ans
#
ans = solution.networkBecomesIdle([[0,1],[0,2],[1,2]], [0,10,10])
assert ans == 3, ans

edges = [[3,8],[4,13],[0,7],[0,4],[1,8],[14,1],[7,2],[13,10],[9,11],[12,14],[0,6],[2,12],[11,5],[6,9],[10,3]]
patience = [0,3,2,1,5,1,5,5,3,1,2,2,2,2,1]
ans = solution.networkBecomesIdle(edges, patience)
assert ans == 20, ans

