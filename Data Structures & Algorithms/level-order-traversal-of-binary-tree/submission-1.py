# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans=[]
        
        queue=deque([root])

        while queue:
            scan_len=len(queue)
            level_val=[]
            for _ in range (scan_len):
                node=queue.popleft()
                level_val.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            ans.append(level_val)
        return ans        
