# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len=0
        def depth(curr):
            nonlocal max_len
            if curr is None:
                return 0
            l_dep=depth(curr.left)
            r_dep=depth(curr.right)
            max_len=max(max_len, l_dep+r_dep)
            return 1+max(l_dep,r_dep)
        depth(root)
        return max_len