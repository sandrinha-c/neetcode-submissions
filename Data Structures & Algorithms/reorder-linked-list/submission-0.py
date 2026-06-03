# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast= head, head
        #先切成兩段
        while fast and fast.next:
            #print (slow.val)
            slow=slow.next
            fast = fast.next.next
            
        head2=slow.next
        slow.next=None 
        
        prev = None
        curr = head2
        while curr:
            #print (curr.val)
            curr_next = curr.next
            curr.next=prev
            prev = curr
            curr= curr_next
        
        f1=head
        f2=prev

        while f1 and f2:
            f1_next=f1.next
            f2_next=f2.next

            f1.next=f2
            f2.next=f1_next

            f1=f1_next
            f2=f2_next
        
     
           
            



             
