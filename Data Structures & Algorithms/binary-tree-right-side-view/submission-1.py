# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans=[]
        queue=deque([root])

        while queue:
            len_lv=len(queue)
            ans.append(queue[len_lv-1].val)
            for _ in range(len_lv):
                
                node=queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return ans
