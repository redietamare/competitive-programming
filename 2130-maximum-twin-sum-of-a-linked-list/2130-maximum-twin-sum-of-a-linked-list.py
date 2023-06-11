# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow:
            nextslow=slow.next
            slow.next=prev
            prev=slow
            slow=nextslow
        left=head
        right=prev
        maxsum=0
        while right:
            summ=left.val+right.val
            maxsum=max(maxsum,summ)
            left=left.next
            right=right.next
        return(maxsum)
            
            
        