# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self,q,p)-> bool:
        if q is None and p is None:
            return True
        if q is None or p is None:
            return False
        if q.val != p.val: 
            return False
        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True 
        left_check=self.isSubtree(root.left, subRoot)
        right_check=self.isSubtree(root.right, subRoot)
        return left_check or right_check 
        