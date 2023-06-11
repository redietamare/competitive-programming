# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=head
        fast=head
        prevslow=head
        prev=None
        if prevslow.next==None:
            dummy.next=head
            dummy.next=prev
            return(dummy.next)
        else:
            while fast and fast.next:
                fast=fast.next.next
                prevslow=slow
                slow=slow.next
            prevslow.next=prevslow.next.next
            return(head)
        