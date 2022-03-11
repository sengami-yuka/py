from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.children = []


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def dfs(node):
            if not node:
                return 0
            for c in node.children:
                node.val += dfs(c)
            return node.val

        L = len(parents)
        bt = [TreeNode(1) for _ in range(L)]
        for i in range(1, L):
            p = parents[i]
            bt[p].children.append(bt[i])
        dfs(bt[0])

        h = 0
        c = 0
        for i in range(L):
            if bt[i].val == 1:
                s = L - 1
            else:
                s = (L - bt[i].val) or 1
                for child in bt[i].children:
                    s *= child.val
            if s > h:
                h = s
                c = 1
            elif s == h:
                c += 1
        return c


class Solution2:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parents[node]].append(node)
        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        dfs(0)
        return cnt


solution = Solution2()
assert 3 == solution.countHighestScoreNodes([-1,2,0,2,0])
assert 2 == solution.countHighestScoreNodes([-1,2,0])
