# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(curr):
            if curr is None:
                return 0,True
            l_dep, l_bal=depth(curr.left)
            r_dep, r_bal=depth(curr.right)
            children_bal=l_bal and r_bal
            bal=abs(l_dep-r_dep)<=1
            return 1+max(l_dep, r_dep),bal and  children_bal
        depth, balanced= depth(root)
        return balanced