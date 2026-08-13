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
            for _ in range(len_lv):
                ans_lv=[]
                node=queue.popleft()
                ans_lv.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(ans_lv)
        
        ans_right_view=[]
        for item in ans:
            ans_right_view.append(item[-1])
        return ans_right_view
