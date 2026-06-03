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
        curr=head
        if head is None:
            return None
        while curr:
            #a>a'>b>b'
            ori_next=curr.next
            curr_copy= Node(curr.val)
            curr.next= curr_copy
            curr_copy.next= ori_next
            curr=curr.next.next
                   
        curr=head
        while curr:
            #hook random curr.next=curr' ; X: curr'.random= curr.random  
            #O: curr'.random = curr_random.next
            if curr.random is not None: 
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr=curr.next.next
        
        old = head
        new_head=head.next
        while old:
            #resume old chain
            copy = old.next
            old.next = copy.next
            #creat new chain of copy  
            if copy.next:
                copy.next=copy.next.next
            else:
                copy.next=None
            old=old.next
            
        return new_head

        