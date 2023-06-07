# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummynode=ListNode()
        dummynode.next=head
        current=dummynode
        while current:
            if current.next!=None and current.next.val==val:
                x=current.next.next
                current.next=x
            else:
                current=current.next
        return(dummynode.next)
        
        