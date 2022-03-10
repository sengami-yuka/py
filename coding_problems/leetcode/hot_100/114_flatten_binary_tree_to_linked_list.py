# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        a = []
        cur = self
        while cur:
            a.append(cur.val)
            cur = cur.right
        return str(a)


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            s.append(node)
            dfs(node.left)
            dfs(node.right)

        s = []
        dfs(root)
        for i in range(len(s) - 1):
            s[i].left = None
            s[i].right = s[i + 1]


class Solution2:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right


solution = Solution2()
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
print(root)
solution.flatten(root)
print(root)
