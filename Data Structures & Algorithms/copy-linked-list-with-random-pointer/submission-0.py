"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #MAPPING
        old_new_map=dict()
        curr=head
        if head is None:
                return None
        
        while curr:
            new_node= Node(curr.val)   
            old_new_map[curr]=new_node
            curr=curr.next
        curr=head
        while curr:
            old_new_map[curr].next=old_new_map.get(curr.next)
            curr=curr.next
        curr=head
        while curr:
            old_new_map[curr].random= old_new_map.get(curr.random)
            curr=curr.next
        return old_new_map[head]