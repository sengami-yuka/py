
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append(cur.val)
            cur = cur.right
            if cur == self:
                break
        return str(a)


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node:
                dfs(node.left)
                st.append(node)
                dfs(node.right)
        if not root:
            return
        st = []
        dfs(root)
        for i in range(len(st)):
            st[i].left = st[i - 1]
            st[i - 1].right = st[i]
        return st[0]


class Solution2:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            nonlocal pre, head
            if node:
                dfs(node.left)
                if not pre:
                    pre = head = node
                else:
                    pre.right, node.left = node, pre
                    pre = node
                dfs(node.right)
        if not root:
            return
        pre = head = None
        dfs(root)
        head.left, pre.right = pre, head
        return head


solution = Solution2()
root = Node(4, Node(2, Node(1), Node(3)), Node(5))
print(root)
ans = solution.treeToDoublyList(root)
print(ans)
