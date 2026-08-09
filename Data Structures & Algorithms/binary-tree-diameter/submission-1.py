# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(curr):
            if curr is None:
                return 0
            
            l_dep=dfs(curr.left)
            r_dep=dfs(curr.right)
            self.ans=max(self.ans, l_dep+r_dep)
            return 1+max(l_dep, r_dep)
        dfs(root)
        return self.ans
