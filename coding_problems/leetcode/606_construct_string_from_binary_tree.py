# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            nonlocal ans
            if node:
                ans += '(%d' % node.val
                if not node.left and node.right:
                    ans += '()'
                    dfs(node.right)
                else:
                    if node.left:
                        dfs(node.left)
                    if node.right:
                        dfs(node.right)
                ans += ')'
        ans = ''
        dfs(root)
        return ans[1:-1]


class Solution2:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"


class Solution3:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        st = [root]
        vis = set()
        while st:
            node = st[-1]
            if node in vis:
                if node != root:
                    ans += ")"
                st.pop()
            else:
                vis.add(node)
                if node != root:
                    ans += "("
                ans += str(node.val)
                if node.left is None and node.right:
                    ans += "()"
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
        return ans


solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
ans = solution.tree2str(root)
assert ans == '1(2(4))(3)', ans

root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
ans = solution.tree2str(root)
assert ans == '1(2()(4))(3)', ans
