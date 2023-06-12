# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current=head
        curr=head
        count=0
        if not head:
            return(head)
        while current:
            count+=1
            current=current.next
        k=k%count
        if k==0:
            return(head)
        else:
            iterate=count-k-1
            for i in range(iterate):
                curr=curr.next
            tail=curr.next
            curr.next=None
            newhead=tail
            while tail:
                pre=tail
                tail=tail.next
            pre.next=head
            return(newhead)


            
        