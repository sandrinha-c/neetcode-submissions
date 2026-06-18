# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        curr_level_nodes=[root]
 
        while curr_level_nodes:
            level_val=[]
            next_level_nodes=[]
            for node in curr_level_nodes:
                level_val.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            ans.append(level_val)
            curr_level_nodes=next_level_nodes
        return ans
