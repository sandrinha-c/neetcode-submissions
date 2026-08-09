# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if curr is None:
                return (0, True)
            l_dep,l_balanced=dfs(curr.left)
            r_dep,r_balanced=dfs(curr.right)
            return 1+max(l_dep, r_dep), abs(l_dep-r_dep)<=1 and (l_balanced and r_balanced
        )
        dep,balanced=dfs(root)
        return balanced
        