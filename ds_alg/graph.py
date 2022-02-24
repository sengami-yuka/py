from collections import defaultdict, deque


class Graph:
    """
        graph, dfs, and bfs
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        visited = set()
        path = []
        stack = []
        stack.append(s)
        visited.add(s)

        while stack:
            s = stack.pop()
            path.append(s)
            for i in self.graph[s]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return path

    def bfs(self, s):
        visited = set()
        path = []
        queue = deque()

        queue.append(s)
        visited.add(s)

        while queue:
            s = queue.popleft()
            path.append(s)
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return path


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print(g.graph)
print(g.bfs(0))
print(g.dfs(2))
