# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        q = collections.deque()
        q.append(self)
        a = []
        while q:
            node = q.popleft()
            if node:
                a.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                a.append(None)
        while a[-1] is None:
            a.pop()
        return str(a)


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = collections.deque([self.root])
        while self.q:
            cur = self.q.popleft()
            if not cur.left or not cur.right:
                self.q.appendleft(cur)
                if cur.left:
                    self.q.append(cur.left)
                break

            else:
                self.q.append(cur.left)
                self.q.append(cur.right)

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        self.q.append(node)
        if not self.q[0].left:
            self.q[0].left = node
            return self.q[0].val
        else:
            self.q[0].right = node
            return self.q.popleft().val

    def get_root(self) -> TreeNode:
        return self.root


ipt = [[[1,2,3,4,5,6]],[7],[8],[]]
out = [None,3,4,[1,2,3,4,5,6,7,8]]
root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6)))
obj = CBTInserter(root)
for i in range(1, len(ipt) - 1):
    ans = obj.insert(*ipt[i])
    assert ans == out[i], (i, ans, out[i])
print(obj.get_root())


ipt = [[[1,2]],[3],[4],[]]
out = [None,1,2,[1,2,3,4]]
root = TreeNode(1,TreeNode(2))
obj = CBTInserter(root)
for i in range(1, len(ipt) - 1):
    ans = obj.insert(*ipt[i])
    assert ans == out[i], (i, ans, out[i])
print(obj.get_root())
